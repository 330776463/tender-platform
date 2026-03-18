<template>
  <div class="home">
    <!-- Header -->
    <header class="header">
      <div class="header-inner">
        <div class="logo">
          <div class="logo-icon">📋</div>
          <span>招标头条</span>
        </div>
        <div class="header-search">
          <select v-model="searchType">
            <option value="all">全站</option>
            <option value="bid">招标</option>
            <option value="result">中标</option>
          </select>
          <input type="text" v-model="keyword" placeholder="搜索招标、中标、项目..." @keyup.enter="handleSearch" />
          <button @click="handleSearch">搜索</button>
        </div>
        <div class="header-actions">
          <el-badge :value="3" class="notification-bell">
            <el-icon><Bell /></el-icon>
          </el-badge>
          <div class="vip-badge">👑 年度VIP</div>
          <el-dropdown>
            <div class="user-avatar">张</div>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item>个人中心</el-dropdown-item>
                <el-dropdown-item>我的收藏</el-dropdown-item>
                <el-dropdown-item>订阅管理</el-dropdown-item>
                <el-dropdown-item divided>退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </div>
    </header>

    <!-- Nav -->
    <nav class="nav">
      <div class="nav-inner">
        <router-link to="/" class="nav-item active">首页</router-link>
        <router-link to="/list" class="nav-item">招标信息</router-link>
        <router-link to="/list?type=result" class="nav-item">中标结果</router-link>
        <router-link to="/list" class="nav-item">采购单位</router-link>
        <router-link to="/list" class="nav-item">行业分类</router-link>
        <router-link to="/vip" class="nav-item vip-link">VIP专区</router-link>
        <router-link to="/subscription" class="nav-item">订阅管理</router-link>
      </div>
    </nav>

    <!-- Main Content -->
    <main class="main">
      <!-- User Section -->
      <div class="user-section">
        <div class="section-grid">
          <div class="subscription-panel">
            <div class="panel-header">
              <span class="panel-title">🎯 我的订阅</span>
              <span class="panel-link">管理订阅 →</span>
            </div>
            <div class="subscription-tags">
              <el-tag type="primary">
                建筑工程 <el-badge value="3" />
              </el-tag>
              <el-tag type="success">
                政府采购 <el-badge value="5" />
              </el-tag>
              <el-tag type="warning">
                医疗设备 <el-badge value="1" />
              </el-tag>
              <el-tag>+ 添加订阅</el-tag>
            </div>
          </div>
          <div class="recommend-panel">
            <div class="panel-header">
              <span class="panel-title">✨ 猜你喜欢</span>
              <span class="panel-hint">基于您的收藏推荐</span>
            </div>
            <div class="recommend-list">
              <div class="recommend-item">
                <span>杭州市智慧城市数据平台建设项目</span>
                <span class="match-rate">匹配度 95%</span>
              </div>
              <div class="recommend-item">
                <span>深圳市某区智慧交通系统扩容</span>
                <span class="match-rate">匹配度 88%</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Filter Bar -->
      <div class="filter-bar">
        <div class="filter-group">
          <span class="filter-label">招标类型</span>
          <div class="filter-options">
            <el-tag v-for="type in tenderTypes" :key="type" :type="type === '全部' ? 'primary' : ''" effect="plain">
              {{ type }}
            </el-tag>
          </div>
        </div>
        <div class="filter-group">
          <span class="filter-label">地区</span>
          <div class="filter-options">
            <el-tag v-for="region in regions" :key="region" effect="plain">
              {{ region }}
            </el-tag>
          </div>
        </div>
      </div>

      <!-- Content -->
      <div class="content-grid">
        <div class="tender-list">
          <div class="list-header">
            <div>
              <span class="list-title">招标信息</span>
              <span class="list-count">找到 1,234 条</span>
            </div>
            <div class="view-toggle">
              <el-button-group>
                <el-button :type="viewMode === 'list' ? 'primary' : 'default'" @click="viewMode = 'list'">
                  <el-icon><List /></el-icon>
                </el-button>
                <el-button :type="viewMode === 'card' ? 'primary' : 'default'" @click="viewMode = 'card'">
                  <el-icon><Grid /></el-icon>
                </el-button>
              </el-button-group>
            </div>
          </div>

          <!-- List View -->
          <div v-if="viewMode === 'list'" class="tender-items">
            <div v-for="item in tenderList" :key="item.id" class="tender-item">
              <div class="tender-header">
                <el-tag :type="getTypeColor(item.type)">{{ item.type }}</el-tag>
                <span class="tender-date">{{ item.date }}</span>
              </div>
              <div class="tender-title">{{ item.title }}</div>
              <div class="tender-meta">
                <span>💰 {{ item.budget }}</span>
                <span>📍 {{ item.region }}</span>
                <span>🌐 {{ item.source }}</span>
              </div>
              <div class="tender-actions">
                <el-button text><el-icon><Star /></el-icon> 收藏</el-button>
                <el-button type="primary" text>详情 →</el-button>
              </div>
            </div>
          </div>

          <!-- Card View -->
          <div v-else class="tender-cards">
            <div v-for="item in tenderList" :key="item.id" class="tender-card">
              <div class="tender-header">
                <el-tag :type="getTypeColor(item.type)" size="small">{{ item.type }}</el-tag>
              </div>
              <div class="card-body">
                <div class="tender-title">{{ item.title }}</div>
                <div class="tender-meta">
                  <span>💰 {{ item.budget }}</span>
                  <span>📍 {{ item.region }}</span>
                </div>
                <span class="tender-date">{{ item.date }}</span>
              </div>
              <div class="card-footer">
                <el-button text size="small"><el-icon><Star /></el-icon></el-button>
                <el-button type="primary" text size="small">详情 →</el-button>
              </div>
            </div>
          </div>

          <div class="pagination">
            <el-pagination background layout="prev, pager, next" :total="1234" />
          </div>
        </div>

        <!-- Sidebar -->
        <aside class="sidebar">
          <div class="sidebar-card">
            <div class="sidebar-title">🏢 热门采购单位</div>
            <div class="hot-unit" v-for="unit in hotUnits" :key="unit.name">
              <span class="hot-unit-name">{{ unit.name }}</span>
              <span class="hot-unit-count">{{ unit.count }}条</span>
            </div>
          </div>
          <div class="sidebar-card">
            <div class="sidebar-title">📊 平台统计</div>
            <div class="stats-grid">
              <div class="stat-item">
                <div class="stat-value">12.8万</div>
                <div class="stat-label">招标信息</div>
              </div>
              <div class="stat-item">
                <div class="stat-value">8.6万</div>
                <div class="stat-label">中标结果</div>
              </div>
              <div class="stat-item">
                <div class="stat-value">2,340</div>
                <div class="stat-label">采购单位</div>
              </div>
              <div class="stat-item">
                <div class="stat-value">156</div>
                <div class="stat-label">今日更新</div>
              </div>
            </div>
          </div>
        </aside>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { Bell, Star, List, Grid } from '@element-plus/icons-vue'

const router = useRouter()

const searchType = ref('all')
const keyword = ref('')
const viewMode = ref('list')

const tenderTypes = ['全部', '招标公告', '中标结果', '采购意向', '变更公告']
const regions = ['全部', '北京', '上海', '广东', '浙江', '江苏', '+ 更多']

const tenderList = ref([
  { id: 1, type: '招标公告', title: '杭州市某区政务服务中心信息化建设项目公开招标公告', budget: '¥1,200,000', region: '浙江省', source: '政府采购网', date: '2026-03-17' },
  { id: 2, type: '中标结果', title: '深圳市某区智慧交通系统建设项目中标结果公示', budget: '¥980,000', region: '广东省', source: '招标平台', date: '2026-03-17' },
  { id: 3, type: '采购意向', title: '某大学2026年度实验室设备采购意向公告', budget: '¥3,500,000', region: '北京市', source: '政府采购网', date: '2026-03-16' },
  { id: 4, type: '变更公告', title: '关于某医院医疗设备采购项目的变更公告', budget: '¥2,800,000', region: '上海市', source: '招标投标网', date: '2026-03-16' },
])

const hotUnits = [
  { name: '杭州市财政局', count: '15,234' },
  { name: '深圳市教育局', count: '12,856' },
  { name: '上海市卫健委', count: '10,421' },
  { name: '广东省公安厅', count: '8,765' },
  { name: '北京市交通局', count: '6,543' },
]

const getTypeColor = (type: string) => {
  const colors: Record<string, string> = {
    '招标公告': 'primary',
    '中标结果': 'success',
    '采购意向': 'warning',
    '变更公告': 'danger'
  }
  return colors[type] || ''
}

const handleSearch = () => {
  router.push({ path: '/list', query: { keyword: keyword.value, type: searchType.value } })
}
</script>

<style scoped>
.header {
  background: #fff;
  border-bottom: 1px solid #f0f0f0;
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-inner {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 24px;
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 20px;
  font-weight: 600;
  color: #1890ff;
}

.logo-icon {
  width: 32px;
  height: 32px;
  background: linear-gradient(135deg, #1890ff, #69c0ff);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 18px;
}

.header-search {
  flex: 1;
  max-width: 600px;
  margin: 0 32px;
  display: flex;
}

.header-search select {
  width: 100px;
  padding: 0 12px;
  border: 1px solid #d9d9d9;
  border-right: none;
  border-radius: 4px 0 0 4px;
  background: #fff;
  font-size: 14px;
}

.header-search input {
  flex: 1;
  padding: 0 12px;
  border: 1px solid #d9d9d9;
  border-left: none;
  font-size: 14px;
  outline: none;
}

.header-search input:focus {
  border-color: #1890ff;
}

.header-search button {
  padding: 0 20px;
  background: #1890ff;
  border: none;
  border-radius: 0 4px 4px 0;
  color: #fff;
  font-size: 14px;
  cursor: pointer;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 16px;
}

.notification-bell {
  cursor: pointer;
  font-size: 20px;
}

.vip-badge {
  background: linear-gradient(135deg, #faad14, #d48806);
  color: #fff;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
}

.user-avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: linear-gradient(135deg, #1890ff, #69c0ff);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-weight: 600;
  cursor: pointer;
  border: 2px solid #faad14;
}

.nav {
  background: #fff;
  border-bottom: 1px solid #f0f0f0;
}

.nav-inner {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  height: 48px;
}

.nav-item {
  display: flex;
  align-items: center;
  padding: 0 24px;
  color: #595959;
  font-weight: 500;
  text-decoration: none;
  transition: color 0.2s;
}

.nav-item:hover,
.nav-item.active {
  color: #1890ff;
}

.nav-item.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: #1890ff;
}

.nav-item.vip-link {
  color: #faad14;
}

.main {
  max-width: 1400px;
  margin: 0 auto;
  padding: 24px;
}

.user-section {
  background: linear-gradient(135deg, #fffbe6 0%, #fff 100%);
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 24px;
  border: 1px solid #ffe58f;
}

.section-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.panel-title {
  font-size: 16px;
  font-weight: 600;
  color: #262626;
}

.panel-link {
  font-size: 12px;
  color: #1890ff;
  cursor: pointer;
}

.panel-hint {
  font-size: 12px;
  color: #8c8c8c;
}

.subscription-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.recommend-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.recommend-item {
  display: flex;
  justify-content: space-between;
  font-size: 13px;
  color: #595959;
}

.match-rate {
  color: #8c8c8c;
}

.filter-bar {
  background: #fff;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 24px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.filter-group {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 12px;
}

.filter-group:last-child {
  margin-bottom: 0;
}

.filter-label {
  font-size: 14px;
  color: #8c8c8c;
  min-width: 60px;
}

.filter-options {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.content-grid {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 24px;
}

.list-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.list-title {
  font-size: 18px;
  font-weight: 600;
}

.list-count {
  margin-left: 12px;
  color: #8c8c8c;
  font-size: 14px;
}

.tender-items {
  background: #fff;
  border-radius: 8px;
  overflow: hidden;
}

.tender-item {
  padding: 16px 20px;
  border-bottom: 1px solid #f0f0f0;
  transition: background 0.2s;
}

.tender-item:hover {
  background: #fafafa;
}

.tender-item:last-child {
  border-bottom: none;
}

.tender-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.tender-title {
  font-size: 15px;
  font-weight: 500;
  color: #262626;
  margin-bottom: 8px;
  line-height: 1.5;
}

.tender-meta {
  display: flex;
  gap: 16px;
  font-size: 13px;
  color: #8c8c8c;
  margin-bottom: 12px;
}

.tender-actions {
  display: flex;
  gap: 8px;
}

.tender-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.tender-card {
  background: #fff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  transition: box-shadow 0.2s;
}

.tender-card:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.10);
}

.tender-card .tender-header {
  padding: 16px 16px 0;
}

.card-body {
  padding: 12px 16px;
}

.card-body .tender-title {
  font-size: 14px;
  margin-bottom: 8px;
}

.card-body .tender-meta {
  margin-bottom: 8px;
}

.tender-date {
  font-size: 12px;
  color: #8c8c8c;
}

.card-footer {
  padding: 12px 16px;
  border-top: 1px solid #f0f0f0;
  display: flex;
  justify-content: space-between;
}

.pagination {
  margin-top: 24px;
  display: flex;
  justify-content: center;
}

.sidebar-card {
  background: #fff;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.sidebar-title {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 16px;
}

.hot-unit {
  display: flex;
  justify-content: space-between;
  padding: 8px 0;
  border-bottom: 1px solid #f0f0f0;
  font-size: 14px;
}

.hot-unit:last-child {
  border-bottom: none;
}

.hot-unit-name {
  color: #262626;
}

.hot-unit-count {
  color: #8c8c8c;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.stat-item {
  text-align: center;
}

.stat-value {
  font-size: 20px;
  font-weight: 600;
  color: #1890ff;
}

.stat-label {
  font-size: 12px;
  color: #8c8c8c;
}
</style>
