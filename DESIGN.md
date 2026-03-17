# 招标信息平台 - 系统设计文档

## 1. 系统架构

### 1.1 整体架构

```
┌─────────────────────────────────────────────────────────────┐
│                        用户访问                              │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                      CDN (可选)                              │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                    Nginx 负载均衡                             │
└─────────┬─────────────────────────┬─────────────────────────┘
          │                         │
┌─────────▼─────────┐     ┌─────────▼─────────┐
│   Vue3 前端       │     │  Spring Boot API  │
│   tender-web      │     │  tender-api       │
└─────────┬─────────┘     └─────────┬─────────┘
          │                         │
          │                   ┌─────▼─────┐
          │                   │   MySQL   │
          │                   └───────────┘
          │
┌─────────▼─────────┐
│   Python 爬虫     │
│   tender-spider  │
└─────────┬─────────┘
          │
    ┌─────▼─────┐
    │   MySQL   │
    └───────────┘
```

### 1.2 技术栈

| 层级 | 技术 | 版本 |
|------|------|------|
| 前端 | Vue 3 | 3.4+ |
| 前端构建 | Vite | 5.0+ |
| 前端UI | Element Plus | 2.5+ |
| 后端 | Spring Boot | 3.2+ |
| 后端Java | Java | 17 |
| 数据库 | MySQL | 8.0 |
| ORM | MyBatis-Plus | 3.5+ |
| 爬虫 | Python | 3.10+ |
| 爬虫框架 | Scrapy | 2.9+ |
| 部署 | Docker | 24.0+ |

### 1.3 项目模块

```
tender-platform/
├── tender-platform-web/     # Vue3 前端
│   ├── src/
│   │   ├── views/          # 页面组件
│   │   ├── components/     # 公共组件
│   │   ├── api/           # API 请求
│   │   ├── router/        # 路由配置
│   │   └── store/         # 状态管理
│   └── package.json
│
├── tender-platform-api/     # Spring Boot 后端
│   ├── src/main/java/
│   │   └── com/tender/
│   │       ├── controller/  # 控制器
│   │       ├── service/    # 业务逻辑
│   │       ├── mapper/     # 数据访问
│   │       ├── entity/    # 实体类
│   │       └── config/    # 配置类
│   └── pom.xml
│
└── tender-platform-spider/  # Python 爬虫
    ├── tender_spider/
    │   ├── spiders/       # 爬虫脚本
    │   ├── pipelines/     # 数据处理
    │   └── items.py      # 数据模型
    └── requirements.txt
```

---

## 2. 数据库设计

### 2.1 招标信息表 (tender)

| 字段 | 类型 | 说明 |
|------|------|------|
| id | BIGINT | 主键 |
| title | VARCHAR(500) | 招标标题 |
| content | TEXT | 招标内容 |
| tender_no | VARCHAR(100) | 招标编号 |
| type | VARCHAR(50) | 招标类型 |
| region | VARCHAR(50) | 地区 |
| province | VARCHAR(50) | 省份 |
| city | VARCHAR(50) | 城市 |
| industry | VARCHAR(50) | 行业分类 |
| source | VARCHAR(100) | 数据来源 |
| source_url | VARCHAR(500) | 原始URL |
| publish_date | DATE | 发布日期 |
| deadline | DATE | 截止日期 |
| budget | DECIMAL(15,2) | 预算金额 |
| status | TINYINT | 状态(1-招标中2-已结束3-已取消) |
| created_at | DATETIME | 创建时间 |
| updated_at | DATETIME | 更新时间 |

### 2.2 采购单位表 (purchaser)

| 字段 | 类型 | 说明 |
|------|------|------|
| id | BIGINT | 主键 |
| name | VARCHAR(200) | 单位名称 |
| region | VARCHAR(50) | 地区 |
| province | VARCHAR(50) | 省份 |
| city | VARCHAR(50) | 城市 |
| type | VARCHAR(50) | 单位类型 |
| contact_name | VARCHAR(50) | 联系人 |
| contact_phone | VARCHAR(20) | 联系电话 |
| contact_email | VARCHAR(100) | 邮箱 |
| address | VARCHAR(200) | 地址 |
| created_at | DATETIME | 创建时间 |
| updated_at | DATETIME | 更新时间 |

### 2.3 中标信息表 (bid_result)

| 字段 | 类型 | 说明 |
|------|------|------|
| id | BIGINT | 主键 |
| tender_id | BIGINT | 招标信息ID |
| tender_no | VARCHAR(100) | 招标编号 |
| winner | VARCHAR(200) | 中标单位 |
| winner_amount | DECIMAL(15,2) | 中标金额 |
| publish_date | DATE | 发布日期 |
| created_at | DATETIME | 创建时间 |
| updated_at | DATETIME | 更新时间 |

### 2.4 用户表 (user)

| 字段 | 类型 | 说明 |
|------|------|------|
| id | BIGINT | 主键 |
| username | VARCHAR(50) | 用户名(唯一) |
| password | VARCHAR(200) | 密码(加密) |
| nickname | VARCHAR(50) | 昵称 |
| email | VARCHAR(100) | 邮箱 |
| phone | VARCHAR(20) | 手机号 |
| avatar | VARCHAR(200) | 头像URL |
| status | TINYINT | 状态(0-禁用1-正常) |
| created_at | DATETIME | 创建时间 |
| updated_at | DATETIME | 更新时间 |

### 2.5 收藏表 (favorite)

| 字段 | 类型 | 说明 |
|------|------|------|
| id | BIGINT | 主键 |
| user_id | BIGINT | 用户ID |
| tender_id | BIGINT | 招标信息ID |
| created_at | DATETIME | 创建时间 |

### 2.6 订阅表 (subscription)

| 字段 | 类型 | 说明 |
|------|------|------|
| id | BIGINT | 主键 |
| user_id | BIGINT | 用户ID |
| keywords | VARCHAR(200) | 关键词 |
| regions | VARCHAR(200) | 地区 |
| industries | VARCHAR(200) | 行业 |
| types | VARCHAR(200) | 招标类型 |
| notify_email | TINYINT | 邮件通知(0-否1-是) |
| notify_sms | TINYINT | 短信通知(0-否1-是) |
| status | TINYINT | 状态(0-禁用1-启用) |
| created_at | DATETIME | 创建时间 |
| updated_at | DATETIME | 更新时间 |

### 2.7 地区表 (region)

| 字段 | 类型 | 说明 |
|------|------|------|
| id | INT | 主键 |
| name | VARCHAR(50) | 地区名称 |
| parent_id | INT | 父级ID |
| level | TINYINT | 层级(1-省2-市3-区) |

### 2.8 行业分类表 (industry)

| 字段 | 类型 | 说明 |
|------|------|------|
| id | INT | 主键 |
| name | VARCHAR(50) | 行业名称 |
| parent_id | INT | 父级ID |
| level | TINYINT | 层级 |

---

## 3. API 接口设计

### 3.1 招标信息

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/tender/list | 招标列表 |
| GET | /api/tender/{id} | 招标详情 |
| GET | /api/tender/search | 搜索招标 |
| GET | /api/tender/types | 招标类型列表 |
| GET | /api/tender/regions | 地区筛选列表 |
| GET | /api/tender/industries | 行业筛选列表 |

### 3.2 中标信息

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/bid/list | 中标列表 |
| GET | /api/bid/{id} | 中标详情 |

### 3.3 用户认证

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | /api/auth/register | 用户注册 |
| POST | /api/auth/login | 用户登录 |
| GET | /api/auth/info | 获取用户信息 |
| POST | /api/auth/logout | 登出 |

### 3.4 用户功能

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/user/favorites | 我的收藏 |
| POST | /api/user/favorite | 添加收藏 |
| DELETE | /api/user/favorite/{id} | 删除收藏 |
| GET | /api/user/subscriptions | 我的订阅 |
| POST | /api/user/subscription | 添加订阅 |
| PUT | /api/user/subscription/{id} | 更新订阅 |
| DELETE | /api/user/subscription/{id} | 删除订阅 |

### 3.5 采购单位

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/purchaser/list | 采购单位列表 |
| GET | /api/purchaser/{id} | 采购单位详情 |

---

## 4. 前端页面设计

### 4.1 页面结构

```
┌─────────────────────────────────────────┐
│              Header (顶部导航)            │
├─────────────────────────────────────────┤
│  Logo  │  搜索框  │  导航  │  用户入口     │
├─────────────────────────────────────────┤
│              Banner (轮播图)              │
├─────────────────────────────────────────┤
│  快捷筛选：类型 | 地区 | 行业              │
├─────────────────────────────────────────┤
│  推荐标讯    最新招标    中标结果          │
│    ↓           ↓           ↓            │
│  列表卡片    列表卡片    列表卡片          │
├─────────────────────────────────────────┤
│              Footer (底部)               │
└─────────────────────────────────────────┘
```

### 4.2 页面列表

| 页面 | 路径 | 说明 |
|------|------|------|
| 首页 | / | 招标信息展示 |
| 招标列表 | /tender | 筛选列表 |
| 招标详情 | /tender/:id | 内容详情 |
| 中标列表 | /bid | 中标信息 |
| 采购单位 | /purchaser | 单位列表 |
| 登录 | /login | 用户登录 |
| 注册 | /register | 用户注册 |
| 个人中心 | /user | 用户中心 |
| 我的收藏 | /user/favorites | 收藏列表 |
| 订阅管理 | /user/subscriptions | 订阅管理 |

### 4.3 UI 设计规范

- 主题色：#1890ff (蓝色)
- 辅助色：#52c41a (绿色)
- 背景色：#f5f5f5
- 卡片圆角：8px
- 间距基准：8px

---

## 5. 部署架构

### 5.1 生产环境

```
                    ┌──────────────┐
                    │    CDN       │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │    Nginx     │
                    │  (负载均衡)   │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
        ┌─────▼─────┐ ┌───▼───┐ ┌─────▼─────┐
        │  API-1    │ │API-2  │ │  API-N   │
        └─────┬─────┘ └───┬───┘ └─────┬─────┘
              │            │            │
              └────────────┼────────────┘
                           │
                    ┌──────▼───────┐
                    │    MySQL     │
                    │  (主从复制)   │
                    └──────────────┘
```

### 5.2 服务器配置建议

| 服务 | 配置 | 数量 |
|------|------|------|
| Nginx | 2C2G | 1 |
| API | 2C4G | 2+ |
| MySQL | 4C8G | 1-2 |
| 爬虫 | 2C4G | 1 |

---

## 6. 开发规范

### 6.1 Git 提交规范

```
<类型>(<模块>): <描述>

类型: feat, fix, docs, style, refactor, test, chore
```

### 6.2 分支策略

- main: 生产分支
- develop: 测试分支
- feature/*: 开发分支
- bugfix/*: 修复分支
