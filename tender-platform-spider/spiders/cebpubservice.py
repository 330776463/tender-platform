"""
中国招标投标公共服务平台爬虫
http://www.cebpubservice.com
"""
import scrapy
import json
import re
from datetime import datetime
from urllib.parse import urljoin, parse_qs, urlparse
import logging

logger = logging.getLogger(__name__)


class CEBPubSpider(scrapy.Spider):
    """中国招标投标公共服务平台爬虫"""
    
    name = 'cebpubservice'
    allowed_domains = ['cebpubservice.com']
    
    # 招标类型映射
    TYPE_MAP = {
        '招标公告': 'bid',
        '中标结果': 'result',
        '采购意向': 'intent',
        '变更公告': 'change',
        '废标公告': 'invalid',
    }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = 1
        self.max_pages = 10
        
    def start_requests(self):
        """初始请求 - 招标公告列表"""
        base_url = "http://www.cebpubservice.com/cinf/api/list"
        
        # 招标公告
        for page in range(1, self.max_pages + 1):
            url = f"{base_url}?pageNo={page}&pageSize=30&channelId=8c8143044d984b88877e9a4e40c30d13"
            yield scrapy.Request(
                url,
                callback=self.parse_list,
                meta={'type': '招标公告', 'page': page}
            )
        
        # 中标结果
        for page in range(1, self.max_pages + 1):
            url = f"{base_url}?pageNo={page}&pageSize=30&channelId=8c8143044d984b88877e9a4e40c30d14"
            yield scrapy.Request(
                url,
                callback=self.parse_list,
                meta={'type': '中标结果', 'page': page}
            )
    
    def parse_list(self, response):
        """解析列表页"""
        try:
            data = json.loads(response.text)
            items = data.get('data', {}).get('list', [])
            
            if not items:
                logger.warning(f"第{response.meta['page']}页无数据")
                return
            
            for item in items:
                detail_url = item.get('url', '')
                if detail_url:
                    # 完整URL
                    if not detail_url.startswith('http'):
                        detail_url = urljoin('http://www.cebpubservice.com', detail_url)
                    
                    yield scrapy.Request(
                        detail_url,
                        callback=self.parse_detail,
                        meta={
                            'type': response.meta.get('type'),
                            'title': item.get('title'),
                            'publish_time': item.get('publishTime'),
                        }
                    )
                    
        except Exception as e:
            logger.error(f"解析列表页失败: {e}")
    
    def parse_detail(self, response):
        """解析详情页"""
        try:
            # 提取正文内容
            content = response.xpath('//div[@class="article-content"]//text()').getall()
            content = '\n'.join([c.strip() for c in content if c.strip()])
            
            # 提取金额
            budget = self.extract_budget(content)
            
            # 提取招标人/代理机构
            tenderer = response.xpath('//span[contains(text(),"招标人")]/following-sibling::span/text()').get()
            agent = response.xpath('//span[contains(text(),"代理机构")]/following-sibling::span/text()').get()
            
            # 地区提取
            region = self.extract_region(response.xpath('//div[@class="article-info"]//text()').getall())
            
            item = {
                'title': response.meta.get('title'),
                'type': self.TYPE_MAP.get(response.meta.get('type'), 'bid'),
                'source': '中国招标投标公共服务平台',
                'source_url': response.url,
                'publish_time': response.meta.get('publish_time'),
                'content': content,
                'budget': budget,
                'tenderer': tenderer,
                'agent': agent,
                'region': region,
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
            r'采购预算[:：]\s*([¥￥]?\s*[\d,]+\.?\d*)\s*[万元]?',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, content)
            if match:
                return match.group(1).replace(',', '')
        return None
    
    def extract_region(self, text_list):
        """提取地区"""
        regions = ['北京', '上海', '广东', '浙江', '江苏', '四川', '湖北', '湖南', '山东', '河南',
                   '河北', '安徽', '福建', '江西', '辽宁', '吉林', '黑龙江', '陕西', '云南', '贵州',
                   '甘肃', '新疆', '内蒙古', '宁夏', '青海', '西藏', '海南', '天津', '重庆']
        
        text = '\n'.join([str(t).strip() for t in text_list])
        
        for region in regions:
            if region in text:
                return region
        return None
