"""
爬虫工具函数
"""
import re
from datetime import datetime, timedelta
from dateutil import parser as date_parser
import pytz


def parse_date(date_str):
    """
    解析各种日期格式
    支持: 2024-01-01, 2024/01/01, 2024年01月01日, 1小时前, 3天前等
    """
    if not date_str:
        return None
    
    date_str = date_str.strip()
    
    # 相对时间
    relative_patterns = [
        (r'(\d+)小时前', lambda m: datetime.now() - timedelta(hours=int(m.group(1)))),
        (r'(\d+)天前', lambda m: datetime.now() - timedelta(days=int(m.group(1)))),
        (r'(\d+)分钟前', lambda m: datetime.now() - timedelta(minutes=int(m.group(1)))),
        (r'刚刚', lambda m: datetime.now()),
    ]
    
    for pattern, handler in relative_patterns:
        match = re.search(pattern, date_str)
        if match:
            return handler(match).strftime('%Y-%m-%d %H:%M:%S')
    
    # 绝对时间
    try:
        dt = date_parser.parse(date_str)
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except:
        pass
    
    # 常见格式
    formats = [
        '%Y-%m-%d %H:%M:%S',
        '%Y-%m-%d',
        '%Y/%m/%d',
        '%Y年%m月%d日',
        '%Y.%m.%d',
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).strftime('%Y-%m-%d %H:%M:%S')
        except:
            continue
    
    return None


def parse_money(money_str):
    """
    解析金额字符串
    返回: (金额数字, 单位)
    """
    if not money_str:
        return None, None
    
    # 清洗
    money_str = money_str.strip().replace(',', '').replace('，', '')
    
    # 单位识别
    unit = '元'
    if '万' in money_str:
        unit = '万元'
        money_str = money_str.replace('万', '')
    elif '千' in money_str:
        unit = '千元'
        money_str = money_str.replace('千', '')
    
    # 提取数字
    match = re.search(r'[\d.]+', money_str)
    if match:
        try:
            return float(match.group()), unit
        except:
            pass
    
    return None, None


def clean_text(text):
    """清洗文本"""
    if not text:
        return ''
    
    # 去除多余空白
    text = re.sub(r'\s+', ' ', text)
    # 去除特殊字符
    text = text.replace('\u3000', ' ').replace('\xa0', ' ')
    
    return text.strip()


def extract_phone(text):
    """提取电话号码"""
    if not text:
        return None
    
    patterns = [
        r'1[3-9]\d{9}',  # 手机号
        r'0\d{2,3}-\d{7,8}',  # 固话
        r'\d{3,4}-\d{3,4}-\d{3,4}',  # 分机
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group()
    
    return None


def extract_email(text):
    """提取邮箱"""
    if not text:
        return None
    
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    match = re.search(pattern, text)
    
    if match:
        return match.group()
    
    return None


def extract_company(text):
    """提取公司名称"""
    if not text:
        return None
    
    # 常见公司后缀
    suffixes = ['有限公司', '股份有限公司', '有限责任公司', 
                '集团有限公司', '投资公司', '贸易公司', '科技有限公司']
    
    for suffix in suffixes:
        pattern = rf'.*{suffix}'
        match = re.search(pattern, text)
        if match:
            return match.group()
    
    return None


# 地区映射
REGION_MAP = {
    '北京': {'province': '北京', 'city': '北京'},
    '上海': {'province': '上海', 'city': '上海'},
    '天津': {'province': '天津', 'city': '天津'},
    '重庆': {'province': '重庆', 'city': '重庆'},
    '浙江': {'province': '浙江', 'cities': ['杭州', '宁波', '温州', '嘉兴', '湖州', '绍兴', '金华', '衢州', '舟山', '台州', '丽水']},
    '江苏': {'province': '江苏', 'cities': ['南京', '苏州', '无锡', '常州', '镇江', '扬州', '泰州', '南通', '盐城', '淮安', '连云港', '徐州']},
    '广东': {'province': '广东', 'cities': ['广州', '深圳', '珠海', '东莞', '佛山', '中山', '惠州', '江门', '湛江', '茂名', '肇庆']},
    '山东': {'province': '山东', 'cities': ['济南', '青岛', '烟台', '威海', '潍坊', '临沂', '济宁', '淄博', '枣庄', '东营']},
    '四川': {'province': '四川', 'cities': ['成都', '绵阳', '德阳', '宜宾', '泸州', '南充', '达州', '乐山', '内江', '自贡']},
    '湖北': {'province': '湖北', 'cities': ['武汉', '宜昌', '襄阳', '荆州', '黄冈', '孝感', '荆门', '鄂州', '咸宁']},
}


def parse_region(text):
    """解析地区"""
    if not text:
        return None, None
    
    for province, data in REGION_MAP.items():
        if province in text:
            cities = data.get('cities', [])
            city = None
            for c in cities:
                if c in text:
                    city = c
                    break
            return province, city
    
    return None, None


# 行业映射
INDUSTRY_KEYWORDS = {
    '工程建设': ['建筑', '工程', '施工', '装修', '装饰', '市政', '园林', '绿化', '监理', '造价'],
    '政府采购': ['政府采购', '采购', '招标'],
    '医疗卫生': ['医疗', '医院', '药品', '器械', '卫生', '保健', '防疫'],
    '教育科技': ['学校', '教育', '培训', '科研', '科技', '实验'],
    '交通运输': ['交通', '公路', '铁路', '桥梁', '隧道', '港口', '航运', '物流'],
    '能源化工': ['电力', '能源', '石油', '煤炭', '化工', '光伏', '风电'],
    '金融银行': ['银行', '保险', '证券', '金融', '投资'],
    '信息技术': ['软件', '硬件', '网络', '信息化', '系统', 'IT', '通信'],
    '农林水利': ['农业', '林业', '水利', '灌溉', '养殖', '畜牧'],
    '冶金矿产': ['冶金', '矿产', '钢铁', '有色金属'],
}


def parse_industry(text):
    """解析行业"""
    if not text:
        return None
    
    text = text.lower()
    
    for industry, keywords in INDUSTRY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                return industry
    
    return None
