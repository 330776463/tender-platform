"""
中国政府采购网爬虫
http://www.ccgp.gov.cn
"""
import scrapy
import json
import re
from datetime import datetime
from urllib.parse import urljoin
import logging

logger = logging.getLogger(__name__)


class CCGPSpider(scrapy.Spider):
    """中国政府采购网爬虫"""
    
    name = 'ccgp'
    allowed_domains = ['ccgp.gov.cn']
    
    TYPE_MAP = {
        '招标公告': 'bid',
        '中标公告': 'result',
        '更正公告': 'change',
    }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = 1
        self.max_pages = 10
    
    def start_requests(self):
        """初始请求"""
        # 招标公告
        base_urls = [
            ('http://www.ccgp.gov.cn/cinf/api/list?pageNo={}&pageSize=30&categoryId=4', '招标公告'),
            ('http://www.ccgp.gov.cn/cinf/api/list?pageNo={}&pageSize=30&categoryId=5', '中标公告'),
            ('http://www.ccgp.gov.cn/cinf/api/list?pageNo={}&pageSize=30&categoryId=6', '更正公告'),
        ]
        
        for base_url, type_name in base_urls:
            for page in range(1, self.max_pages + 1):
                url = base_url.format(page)
                yield scrapy.Request(
                    url,
                    callback=self.parse_list,
                    meta={'type': type_name, 'page': page}
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
                    if not detail_url.startswith('http'):
                        detail_url = urljoin('http://www.ccgp.gov.cn', detail_url)
                    
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
            content = response.xpath('//div[@class="article-content"]//text()').getall()
            content = '\n'.join([c.strip() for c in content if c.strip()])
            
            budget = self.extract_budget(content)
            
            # 采购人
            purchaser = response.xpath(
                '//span[contains(text(),"采购人")]/following-sibling::span/text() | '
                '//span[contains(text(),"采购单位")]/following-sibling::span/text()'
            ).get()
            
            # 代理机构
            agent = response.xpath(
                '//span[contains(text(),"代理机构")]/following-sibling::span/text() | '
                '//span[contains(text(),"采购代理机构")]/following-sibling::span/text()'
            ).get()
            
            item = {
                'title': response.meta.get('title'),
                'type': self.TYPE_MAP.get(response.meta.get('type'), 'bid'),
                'source': '中国政府采购网',
                'source_url': response.url,
                'publish_time': response.meta.get('publish_time'),
                'content': content,
                'budget': budget,
                'tenderer': purchaser,
                'agent': agent,
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
            r'金额[:：]\s*([¥￥]?\s*[\d,]+\.?\d*)\s*[万元]?',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, content)
            if match:
                return match.group(1).replace(',', '')
        return None
