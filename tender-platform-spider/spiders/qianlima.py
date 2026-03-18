"""
千里马招标网爬虫
http://www.qianlima.com
"""
import scrapy
import re
from datetime import datetime
from urllib.parse import urljoin
import logging

logger = logging.getLogger(__name__)


class QianlimaSpider(scrapy.Spider):
    """千里马招标网爬虫"""
    
    name = 'qianlima'
    allowed_domains = ['qianlima.com']
    
    TYPE_MAP = {
        '招标公告': 'bid',
        '中标公告': 'result',
        '变更公告': 'change',
        '废标公告': 'invalid',
    }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_pages = 20
    
    def start_requests(self):
        """初始请求"""
        # 各类型列表页
        categories = [
            ('http://www.qianlima.com/zbxx/index_{}.html', '招标公告'),
            ('http://www.qianlima.com/zbxx_1/index_{}.html', '中标公告'),
            ('http://www.qianlima.com/zbxx_2/index_{}.html', '变更公告'),
        ]
        
        for base_url, type_name in categories:
            for page in range(1, self.max_pages + 1):
                url = base_url.format(page)
                yield scrapy.Request(
                    url,
                    callback=self.parse_list,
                    meta={'type': type_name}
                )
    
    def parse_list(self, response):
        """解析列表页"""
        try:
            # 招标信息列表
            items = response.xpath('//div[@class="list_box"]//li | //table[@class="list_table"]//tr')
            
            if not items:
                logger.warning(f"列表页无数据: {response.url}")
                return
            
            for item in items:
                title = item.xpath('.//a[@class="title"]/text() | .//td[@class="title"]//a/text()').get()
                detail_url = item.xpath('.//a[@class="title"]/@href | .//td[@class="title"]//a/@href').get()
                date = item.xpath('.//span[@class="date"]/text() | .//td[@class="date"]/text()').get()
                
                if title and detail_url:
                    if not detail_url.startswith('http'):
                        detail_url = urljoin('http://www.qianlima.com', detail_url)
                    
                    yield scrapy.Request(
                        detail_url,
                        callback=self.parse_detail,
                        meta={
                            'type': response.meta.get('type'),
                            'title': title.strip(),
                            'date': date,
                        }
                    )
                    
        except Exception as e:
            logger.error(f"解析列表页失败: {e}")
    
    def parse_detail(self, response):
        """解析详情页"""
        try:
            # 正文内容
            content = response.xpath(
                '//div[@class="content_box"]//text() | '
                '//div[@id="content"]//text() | '
                '//div[@class="detail_content"]//text()'
            ).getall()
            content = '\n'.join([c.strip() for c in content if c.strip()])
            
            # 提取金额
            budget = self.extract_budget(content)
            
            # 地区
            region = self.extract_region(content)
            
            # 行业
            industry = self.extract_industry(content)
            
            item = {
                'title': response.meta.get('title'),
                'type': self.TYPE_MAP.get(response.meta.get('type'), 'bid'),
                'source': '千里马招标网',
                'source_url': response.url,
                'publish_time': response.meta.get('date'),
                'content': content[:5000],  # 限制长度
                'budget': budget,
                'region': region,
                'industry': industry,
                'create_time': datetime.now().isoformat(),
                'is_valid': 1,
            }
            
            yield item
            
        except Exception as e:
            logger.error(f"解析详情页失败: {e}")
    
    def extract_budget(self, content):
        """提取预算金额"""
        patterns = [
            r'预算[额资金]?[:：]\s*([¥￥]?\s*[\d,]+\.?\d*)\s*[万元]?',
            r'最高限价[:：]\s*([¥￥]?\s*[\d,]+\.?\d*)\s*[万元]?',
            r'项目预算[:：]\s*([¥￥]?\s*[\d,]+\.?\d*)\s*[万元]?',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, content)
            if match:
                return match.group(1).replace(',', '')
        return None
    
    def extract_region(self, content):
        """提取地区"""
        regions = ['北京', '上海', '广东', '浙江', '江苏', '四川', '湖北', '湖南', '山东', '河南',
                   '河北', '安徽', '福建', '江西', '辽宁', '吉林', '黑龙江', '陕西', '云南', '贵州']
        
        for region in regions:
            if region in content:
                return region
        return None
    
    def extract_industry(self, content):
        """提取行业"""
        industries = {
            '建筑': ['建筑', '工程', '装修', '装饰'],
            '医疗': ['医疗', '医院', '药品', '器械'],
            '教育': ['学校', '教育', '培训', '教材'],
            'IT': ['软件', '硬件', '网络', '信息化', '系统'],
            '交通': ['交通', '公路', '铁路', '桥梁', '隧道'],
            '能源': ['电力', '能源', '石油', '煤炭', '光伏'],
            '金融': ['银行', '保险', '证券', '金融'],
        }
        
        for industry, keywords in industries.items():
            for keyword in keywords:
                if keyword in content:
                    return industry
        return None
