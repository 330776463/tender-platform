#!/usr/bin/env python3
"""
招标信息爬虫启动脚本
"""
import os
import sys
import subprocess
from datetime import datetime

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run_spider(spider_name, settings='tender_platform_spider.settings'):
    """运行单个爬虫"""
    cmd = [
        'scrapy', 'crawl', spider_name,
        '--set', f'REDIRECT_ENABLED=False',
        '--set', f'LOG_FILE=logs/{spider_name}_{datetime.now().strftime("%Y%m%d")}.log',
    ]
    
    print(f"启动爬虫: {spider_name}")
    result = subprocess.run(cmd, cwd=os.path.dirname(os.path.abspath(__file__)))
    return result.returncode == 0


def run_all_spiders():
    """运行所有爬虫"""
    spiders = [
        'cebpubservice',  # 中国招标投标公共服务平台
        'ccgp',           # 中国政府采购网
        'qianlima',       # 千里马招标网
    ]
    
    # 确保日志目录存在
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    success_count = 0
    for spider in spiders:
        if run_spider(spider):
            success_count += 1
    
    print(f"\n爬虫执行完成: {success_count}/{len(spiders)} 成功")
    return success_count == len(spiders)


def main():
    """主函数"""
    if len(sys.argv) > 1:
        # 运行指定爬虫
        spider_name = sys.argv[1]
        run_spider(spider_name)
    else:
        # 运行所有爬虫
        run_all_spiders()


if __name__ == '__main__':
    main()
