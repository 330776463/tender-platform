"""
数据处理管道
"""
import pymysql
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class TenderPipeline:
    """招标信息入库管道"""
    
    def __init__(self, settings):
        self.settings = settings
        self.conn = None
        self.cursor = None
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)
    
    def open_spider(self, spider):
        """爬虫启动时连接数据库"""
        try:
            self.conn = pymysql.connect(
                host=self.settings.get('MYSQL_HOST', 'localhost'),
                port=self.settings.get('MYSQL_PORT', 3306),
                user=self.settings.get('MYSQL_USER', 'root'),
                password=self.settings.get('MYSQL_PASSWORD', 'root'),
                database=self.settings.get('MYSQL_DATABASE', 'tender_platform'),
                charset='utf8mb4'
            )
            self.cursor = self.conn.cursor()
            logger.info("数据库连接成功")
        except Exception as e:
            logger.error(f"数据库连接失败: {e}")
    
    def close_spider(self, spider):
        """爬虫关闭时关闭数据库连接"""
        if self.conn:
            self.conn.close()
            logger.info("数据库连接已关闭")
    
    def process_item(self, item, spider):
        """处理每条数据"""
        try:
            # 检查是否已存在
            sql = "SELECT id FROM t_tender WHERE source_url = %s"
            self.cursor.execute(sql, (item.get('source_url'),))
            result = self.cursor.fetchone()
            
            if result:
                # 更新
                sql = """
                    UPDATE t_tender 
                    SET title=%s, type=%s, budget=%s, region=%s, industry=%s,
                        publish_time=%s, deadline=%s, content=%s, update_time=%s
                    WHERE source_url=%s
                """
                self.cursor.execute(sql, (
                    item.get('title'),
                    item.get('type'),
                    item.get('budget'),
                    item.get('region'),
                    item.get('industry'),
                    item.get('publish_time'),
                    item.get('deadline'),
                    item.get('content'),
                    datetime.now(),
                    item.get('source_url')
                ))
            else:
                # 插入
                sql = """
                    INSERT INTO t_tender (
                        title, tender_no, type, status, budget, region, province, city,
                        industry, category, publish_time, deadline, open_time,
                        tenderer, tenderer_contact, agent, agent_contact,
                        winner, win_bid, source, source_url, content,
                        create_time, update_time, is_valid
                    ) VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, %s, %s, %s, %s,
                        %s, %s, %s
                    )
                """
                self.cursor.execute(sql, (
                    item.get('title'),
                    item.get('tender_no'),
                    item.get('type'),
                    item.get('status'),
                    item.get('budget'),
                    item.get('region'),
                    item.get('province'),
                    item.get('city'),
                    item.get('industry'),
                    item.get('category'),
                    item.get('publish_time'),
                    item.get('deadline'),
                    item.get('open_time'),
                    item.get('tenderer'),
                    item.get('tenderer_contact'),
                    item.get('agent'),
                    item.get('agent_contact'),
                    item.get('winner'),
                    item.get('win_bid'),
                    item.get('source'),
                    item.get('source_url'),
                    item.get('content'),
                    datetime.now(),
                    datetime.now(),
                    1
                ))
            
            self.conn.commit()
            return item
            
        except Exception as e:
            self.conn.rollback()
            logger.error(f"数据入库失败: {e}")
            return item


class DuplicatesPipeline:
    """去重管道"""
    
    def __init__(self):
        self.urls_seen = set()
    
    def process_item(self, item, spider):
        if item.get('source_url') in self.urls_seen:
            spider.logger.debug(f"重复数据: {item.get('source_url')}")
            return item
        self.urls_seen.add(item.get('source_url'))
        return item
