<template>
  <div class="list-view">
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
          <div class="user-avatar">张</div>
        </div>
      </div>
    </header>

    <nav class="nav">
      <div class="nav-inner">
        <router-link to="/" class="nav-item">首页</router-link>
        <router-link to="/list" class="nav-item active">招标信息</router-link>
        <router-link to="/list?type=result" class="nav-item">中标结果</router-link>
        <router-link to="/list" class="nav-item">采购单位</router-link>
        <router-link to="/list" class="nav-item">行业分类</router-link>
        <router-link to="/vip" class="nav-item vip-link">VIP专区</router-link>
        <router-link to="/subscription" class="nav-item">订阅管理</router-link>
      </div>
    </nav>

    <main class="main">
      <div class="breadcrumb">
        <router-link to="/">首页</router-link> > <span>招标信息</span>
      </div>

      <div class="filter-bar">
        <el-select v-model="typeFilter" placeholder="全部类型" style="width: 120px">
          <el-option label="全部类型" value="" />
          <el-option label="招标公告" value="bid" />
          <el-option label="中标结果" value="result" />
          <el-option label="采购意向" value="intent" />
        </el-select>
        <el-select v-model="regionFilter" placeholder="全部地区" style="width: 120px">
          <el-option label="全部地区" value="" />
          <el-option label="北京" value="beijing" />
          <el-option label="上海" value="shanghai" />
          <el-option label="广东" value="guangdong" />
          <el-option label="浙江" value="zhejiang" />
        </el-select>
        <el-select v-model="industryFilter" placeholder="全部行业" style="width: 120px">
          <el-option label="全部行业" value="" />
          <el-option label="工程建设" value="engineering" />
          <el-option label="政府采购" value="procurement" />
          <el-option label="医疗卫生" value="medical" />
        </el-select>
        <el-button>清空</el-button>
        <div style="flex: 1"></div>
        <el-input v-model="keyword" placeholder="关键词搜索" style="width: 200px" />
        <el-button type="primary">搜索</el-button>
        <el-button-group style="margin-left: 12px">
          <el-button :type="viewMode === 'list' ? 'primary' : 'default'" @click="viewMode = 'list'">
            <el-icon><List /></el-icon>
          </el-button>
          <el-button :type="viewMode === 'card' ? 'primary' : 'default'" @click="viewMode = 'card'">
            <el-icon><Grid /></el-icon>
          </el-button>
        </el-button-group>
      </div>

      <div class="result-count">找到 1,234 条</div>

      <div class="content">
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
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Bell, Star, List, Grid } from '@element-plus/icons-vue'

const searchType = ref('all')
const keyword = ref('')
const viewMode = ref('list')
const typeFilter = ref('')
const regionFilter = ref('')
const industryFilter = ref('')

const tenderList = ref([
  { id: 1, type: '招标公告', title: '杭州市某区政务服务中心信息化建设项目公开招标公告', budget: '¥1,200,000', region: '浙江省', source: '政府采购网', date: '2026-03-17' },
  { id: 2, type: '中标结果', title: '深圳市某区智慧交通系统建设项目中标结果公示', budget: '¥980,000', region: '广东省', source: '招标平台', date: '2026-03-17' },
  { id: 3, type: '采购意向', title: '某大学2026年度实验室设备采购意向公告', budget: '¥3,500,000', region: '北京市', source: '政府采购网', date: '2026-03-16' },
  { id: 4, type: '变更公告', title: '关于某医院医疗设备采购项目的变更公告', budget: '¥2,800,000', region: '上海市', source: '招标投标网', date: '2026-03-16' },
])

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
  console.log('Search:', keyword.value, searchType.value)
}
</script>

<style scoped>
.header, .nav, .main { composes: --; }
</style>
