"""
爬虫配置文件
"""
import os

# 数据库配置
MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'root')
MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE', 'tender_platform')

# Scrapy配置
BOT_NAME = "tender_spider"
ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 16
DOWNLOAD_DELAY = 1
COOKIES_ENABLED = False

# 代理配置
HTTPPROXY_ENABLED = True
RETRY_ENABLED = True
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 429]

# 请求头
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

# User-Agent
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
]

# 中间件
DOWNLOADER_MIDDLEWARES = {
    'tender_platform_spider.middlewares.RandomUserAgentMiddleware': 400,
    'tender_platform_spider.middlewares.ProxyMiddleware': 410,
}

# 管道
ITEM_PIPELINES = {
    'tender_platform_spider.pipelines.DuplicatesPipeline': 100,
    'tender_platform_spider.pipelines.TenderPipeline': 300,
}

# 日志
LOG_LEVEL = 'INFO'
LOG_FILE = 'logs/spider.log'

# 自动限速
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
