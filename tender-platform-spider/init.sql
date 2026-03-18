-- 招标信息平台数据库初始化脚本
-- 创建数据库
CREATE DATABASE IF NOT EXISTS tender_platform DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE tender_platform;

-- 招标信息表
CREATE TABLE IF NOT EXISTS t_tender (
    id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '主键ID',
    title VARCHAR(500) NOT NULL COMMENT '标题',
    tender_no VARCHAR(100) COMMENT '招标编号',
    type TINYINT COMMENT '类型: 1-招标公告 2-中标结果 3-采购意向 4-变更公告 5-废标公告',
    status TINYINT COMMENT '状态: 1-报名中 2-已截止 3-已开标',
    budget BIGINT COMMENT '预算金额(分)',
    budget_display VARCHAR(50) COMMENT '预算金额(显示)',
    region VARCHAR(50) COMMENT '地区',
    province VARCHAR(50) COMMENT '省份',
    city VARCHAR(50) COMMENT '城市',
    industry VARCHAR(50) COMMENT '行业',
    category VARCHAR(50) COMMENT '分类',
    publish_time DATETIME COMMENT '发布时间',
    deadline DATETIME COMMENT '报名截止时间',
    open_time DATETIME COMMENT '开标时间',
    tenderer VARCHAR(200) COMMENT '招标人',
    tenderer_contact VARCHAR(200) COMMENT '招标人联系方式',
    agent VARCHAR(200) COMMENT '代理机构',
    agent_contact VARCHAR(200) COMMENT '代理机构联系方式',
    winner VARCHAR(200) COMMENT '中标人',
    win_bid BIGINT COMMENT '中标金额(分)',
    win_bid_display VARCHAR(50) COMMENT '中标金额(显示)',
    source VARCHAR(100) COMMENT '来源网站',
    source_url VARCHAR(500) COMMENT '原文链接',
    content TEXT COMMENT '正文内容',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    is_valid TINYINT DEFAULT 1 COMMENT '是否有效: 0-无效 1-有效',
    deleted TINYINT DEFAULT 0 COMMENT '逻辑删除: 0-未删除 1-已删除',
    INDEX idx_type (type),
    INDEX idx_region (region),
    INDEX idx_industry (industry),
    INDEX idx_publish_time (publish_time),
    INDEX idx_source (source),
    INDEX idx_source_url (source_url),
    INDEX idx_create_time (create_time)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='招标信息表';

-- 数据源配置表
CREATE TABLE IF NOT EXISTS t_tender_source (
    id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '主键ID',
    name VARCHAR(100) NOT NULL COMMENT '网站名称',
    code VARCHAR(50) NOT NULL COMMENT '代码标识',
    url VARCHAR(500) COMMENT '列表页URL',
    type VARCHAR(50) COMMENT '网站类型',
    industry VARCHAR(50) COMMENT '行业分类',
    priority TINYINT DEFAULT 3 COMMENT '优先级: 1-高 2-中 3-低',
    enabled TINYINT DEFAULT 1 COMMENT '是否启用: 0-禁用 1-启用',
    last_crawl_time DATETIME COMMENT '上次抓取时间',
    last_crawl_status TINYINT COMMENT '上次抓取状态: 0-失败 1-成功',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_enabled (enabled),
    INDEX idx_priority (priority)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='数据源配置表';

-- 用户表
CREATE TABLE IF NOT EXISTS t_user (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL COMMENT '用户名',
    phone VARCHAR(20) COMMENT '手机号',
    email VARCHAR(100) COMMENT '邮箱',
    password VARCHAR(128) COMMENT '密码',
    avatar VARCHAR(255) COMMENT '头像',
    vip_level TINYINT DEFAULT 0 COMMENT 'VIP等级: 0-普通 1-月度VIP 2-年度VIP 3-企业VIP',
    vip_expire_time DATETIME COMMENT 'VIP过期时间',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted TINYINT DEFAULT 0,
    INDEX idx_phone (phone),
    INDEX idx_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';

-- 收藏表
CREATE TABLE IF NOT EXISTS t_collect (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT NOT NULL,
    tender_id BIGINT NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uk_user_tender (user_id, tender_id),
    INDEX idx_user_id (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='收藏表';

-- 订阅表
CREATE TABLE IF NOT EXISTS t_subscription (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT NOT NULL,
    keyword VARCHAR(100) COMMENT '关键词',
    industry VARCHAR(50) COMMENT '行业',
    region VARCHAR(50) COMMENT '地区',
    push_type TINYINT DEFAULT 1 COMMENT '推送方式: 1-即时 2-每日汇总',
    status TINYINT DEFAULT 1 COMMENT '状态: 0-暂停 1-启用',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_user_id (user_id),
    INDEX idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='订阅表';

-- 消息通知表
CREATE TABLE IF NOT EXISTS t_notification (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT NOT NULL,
    title VARCHAR(200) NOT NULL,
    content TEXT,
    type TINYINT COMMENT '类型: 1-新标讯 2-系统通知 3-会员通知',
    is_read TINYINT DEFAULT 0 COMMENT '是否已读',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_user_id (user_id),
    INDEX idx_is_read (is_read)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='消息通知表';

-- 插入默认数据源
INSERT INTO t_tender_source (name, code, url, type, industry, priority) VALUES
('中国招标投标公共服务平台', 'cebpubservice', 'http://www.cebpubservice.com/cinf/api/list', 'official', '全行业', 1),
('中国政府采购网', 'ccgp', 'http://www.ccgp.gov.cn/cinf/api/list', 'official', '政府采购', 1),
('千里马招标网', 'qianlima', 'http://www.qianlima.com/zbxx/', 'commercial', '全行业', 1),
('浙江省政府采购网', 'zjzfcg', 'http://www.zjzfcg.gov.cn/', 'official', '政府采购', 2),
('广东省政府采购网', 'gdgpo', 'http://www.gdgpo.gov.cn/', 'official', '政府采购', 2);
