"""
招标信息数据模型
"""
import scrapy
from datetime import datetime


class TenderItem(scrapy.Item):
    """招标信息Item"""
    # 基本信息
    title = scrapy.Field()           # 标题
    tender_no = scrapy.Field()       # 招标编号
    type = scrapy.Field()            # 类型：招标公告、中标结果、采购意向等
    status = scrapy.Field()          # 状态：报名中、已截止、已开标
    
    # 金额与地区
    budget = scrapy.Field()           # 预算金额
    region = scrapy.Field()          # 地区
    province = scrapy.Field()        # 省份
    city = scrapy.Field()            # 城市
    
    # 行业分类
    industry = scrapy.Field()        # 行业
    category = scrapy.Field()         # 分类
    
    # 时间信息
    publish_time = scrapy.Field()     # 发布时间
    deadline = scrapy.Field()         # 报名截止时间
    open_time = scrapy.Field()        # 开标时间
    
    # 主体信息
    tenderer = scrapy.Field()        # 招标人
    tenderer_contact = scrapy.Field() # 招标人联系方式
    agent = scrapy.Field()            # 代理机构
    agent_contact = scrapy.Field()    # 代理机构联系方式
    winner = scrapy.Field()           # 中标人（中标结果）
    win_bid = scrapy.Field()         # 中标金额
    
    # 来源
    source = scrapy.Field()           # 来源网站
    source_url = scrapy.Field()       # 原文链接
    content = scrapy.Field()           # 正文内容
    
    # 元数据
    create_time = scrapy.Field()      # 采集时间
    update_time = scrapy.Field()      # 更新时间
    is_valid = scrapy.Field()         # 是否有效


class TenderSource(scrapy.Item):
    """数据源配置"""
    name = scrapy.Field()             # 网站名称
    code = scrapy.Field()             # 代码标识
    url = scrapy.Field()              # 列表页URL
    type = scrapy.Field()             # 网站类型
    industry = scrapy.Field()         # 行业分类
    priority = scrapy.Field()          # 优先级
    enabled = scrapy.Field()          # 是否启用
    cookies = scrapy.Field()          # 必要Cookie
    headers = scrapy.Field()          # 必要Header
