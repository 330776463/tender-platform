# Figma 设计稿导入指南

## 快速开始

### 方法1：手动创建（推荐）

1. 打开 Figma (https://figma.com)
2. 创建新项目
3. 按照下方规范创建组件

### 方法2：导入现有设计

Figma 支持导入：
- Sketch 文件 (.sketch)
- Adobe XD (.xd)
- PDF (.pdf)
- 图片 (.png, .jpg, .svg)

---

## 设计稿结构

```
招标信息平台/
├── 组件库/
│   ├── 按钮/
│   │   ├── Button-Primary
│   │   ├── Button-Default
│   │   └── Button-Text
│   ├── 卡片/
│   │   ├── TenderCard
│   │   └── TenderListItem
│   ├── 筛选/
│   │   ├── FilterBar
│   │   └── SearchBar
│   ├── 标签/
│   │   └── TypeTag
│   └── 导航/
│       ├── Header
│       ├── Nav
│       └── Footer
│
├── 页面/
│   ├── 首页
│   ├── 列表页
│   ├── 详情页
│   ├── 用户中心
│   └── 登录注册
│
└── 样式/
    ├── 色彩
    ├── 字体
    └── 间距
```

---

## 色彩变量 (Figma Variables)

```
/Colors/Primary
- Primary: #1890ff
- Primary Hover: #096dd9
- Primary Active: #0050b3
- Primary Light: #e6f7ff

/Colors/Status
- Success: #52c41a
- Warning: #faad14
- Error: #ff4d4f
- Info: #13c2c2

/Colors/Neutral
- Text Primary: #262626
- Text Secondary: #8c8c8c
- Border: #d9d9d9
- Background: #f5f5f5

/Colors/Tag
- 招标公告: #1890ff
- 中标结果: #52c41a
- 采购意向: #fa8c16
- 变更公告: #ff4d4f
- 废标公告: #8c8c8c
```

---

## 字体样式 (Text Styles)

```
/Heading/H1
- Font: PingFang SC
- Size: 32px
- Weight: 600
- Line Height: 40px

/Heading/H2
- Font: PingFang SC
- Size: 24px
- Weight: 600
- Line Height: 32px

/Heading/H3
- Font: PingFang SC
- Size: 20px
- Weight: 600
- Line Height: 28px

/Body/Body
- Font: PingFang SC
- Size: 14px
- Weight: 400
- Line Height: 22px

/Body/Body Small
- Font: PingFang SC
- Size: 13px
- Weight: 400
- Line Height: 20px

/Caption/Caption
- Font: PingFang SC
- Size: 12px
- Weight: 400
- Line Height: 18px
```

---

## 组件设计规格

### 1. 主按钮 Primary Button

```
Frame: 120 × 40px
Background: #1890ff
Corner Radius: 4px
Text: PingFang SC Medium 14px #FFFFFF
States:
  - Hover: #096dd9
  - Active: #0050b3
  - Disabled: #d9d9d9
```

### 2. 卡片 TenderCard

```
Frame: 380 × 160px
Background: #FFFFFF
Corner Radius: 8px
Shadow: 0 2px 8px rgba(0,0,0,0.06)
Padding: 20px
Elements:
  - Tag: 40 × 24px, corner 4px
  - Title: H3, max 2 lines
  - Meta: Caption, color #8c8c8c
Hover State:
  - Transform: translateY(-2px)
  - Shadow: 0 4px 16px rgba(0,0,0,0.10)
```

### 3. 列表项 TenderListItem

```
Frame: Full Width × 100px
Border Bottom: 1px #f0f0f0
Padding: 16px 20px
Elements:
  - Type Tag: left, 40 × 24px
  - Title: H4, max 1 line
  - Details: Body Small, #8c8c8c
  - Actions: right,收藏/详情
Hover: background #fafafa
```

### 4. 筛选标签 FilterItem

```
Frame: auto × 32px
Padding: 4px 12px
Corner Radius: 4px
Text: 13px
States:
  - Default: #595959, border #d9d9d9
  - Hover: #1890ff, border #1890ff
  - Active: #e6f7ff background, #1890ff text
```

### 5. 搜索框 SearchBar

```
Frame: 400 × 40px
Border: 1px #d9d9d9
Corner Radius: 4px
Padding: 0 12px
Focus:
  - Border: #1890ff
  - Shadow: 0 0 0 2px rgba(24,144,255,0.2)
Icon: 搜索图标 16px #8c8c8c
```

### 6. 顶部导航 Header

```
Frame: Full Width × 64px
Background: #FFFFFF
Shadow: 0 2px 8px rgba(0,0,0,0.06)
Elements:
  - Logo: 24px #1890ff, bold
  - Search: 400 × 36px
  - Nav Links: 14px #8c8c8c
  - User: 登录/注册 14px #1890ff
```

### 7. 底部 Footer

```
Frame: Full Width × 120px
Background: #262626
Text: 14px #8c8c8c
Padding: 32px 24px
Elements:
  - Links: 24px gap
  - Copyright: centered
```

---

## 页面设计

### 首页 Layout

```
Canvas: 1440 × 900px (可滚动)

Header: 1440 × 64px
Filter Bar: 1440 × 120px
Content:
  - Section 1 (推荐标讯): 3 columns
  - Section 2 (最新招标): 列表
  - Section 3 (中标结果): 列表
Pagination: centered
Footer: 1440 × 120px
```

### 列表页 Layout

```
Breadcrumb: 60px
Filter: 80px
Results Header: 60px
List: flexible
Pagination: 80px
```

### 详情页 Layout

```
Breadcrumb: 60px
Title Section: 300px
Content Tabs: 60px
Content Body: flexible
Related: 400px
```

---

## 响应式断点

| 设备 | 宽度 | 列数 |
|------|------|------|
| Desktop | ≥1200px | 3列 |
| Tablet | 768-1199px | 2列 |
| Mobile | <768px | 1列 |

---

## 交互规范

### 页面切换
- Transition: 200ms ease
- Opacity: 0 → 1

### 悬浮效果
- Duration: 200ms
- Easing: ease-out
- Transform: translateY(-2px)

### 按钮点击
- Duration: 100ms
- Scale: 0.98

---

## 导出设置

### 导出格式
- Icons: SVG
- Images: PNG @2x
- Components: SVG

### 导出路径
```
exports/
├── icons/
├── buttons/
└── cards/
```

---

## 资源链接

- Figma 官网: https://figma.com
- Figma 社区: https://www.figma.com/community
- Element Plus (参考): https://element-plus.org
- Ant Design (参考): https://ant.design
