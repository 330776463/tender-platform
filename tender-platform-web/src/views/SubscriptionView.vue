<template>
  <div class="subscription-view">
    <header class="header">
      <div class="header-inner">
        <router-link to="/" class="logo">
          <div class="logo-icon">📋</div>
          <span>招标头条</span>
        </router-link>
        <div class="header-actions">
          <div class="user-avatar">张</div>
        </div>
      </div>
    </header>

    <main class="main">
      <div class="page-header">
        <h2>我的订阅</h2>
        <el-button type="primary">+ 新建订阅</el-button>
      </div>

      <div class="subscription-list">
        <div class="subscription-item">
          <div class="sub-info">
            <div class="sub-tags">
              <el-tag type="primary">🔍 建筑工程</el-tag>
              <el-tag type="success">启用中</el-tag>
            </div>
            <div class="sub-detail">行业: 工程建设 | 地区: 全国 | 推送: 即时</div>
          </div>
          <div class="sub-actions">
            <el-button>编辑</el-button>
            <el-button>暂停</el-button>
            <el-button type="danger">删除</el-button>
          </div>
        </div>

        <div class="subscription-item">
          <div class="sub-info">
            <div class="sub-tags">
              <el-tag type="success">🔍 政府采购</el-tag>
              <el-tag type="success">启用中</el-tag>
            </div>
            <div class="sub-detail">行业: 政府采购 | 地区: 浙江省 | 推送: 每日汇总</div>
          </div>
          <div class="sub-actions">
            <el-button>编辑</el-button>
            <el-button>暂停</el-button>
            <el-button type="danger">删除</el-button>
          </div>
        </div>

        <div class="subscription-item">
          <div class="sub-info">
            <div class="sub-tags">
              <el-tag type="warning">🔍 医疗设备</el-tag>
              <el-tag>已暂停</el-tag>
            </div>
            <div class="sub-detail">行业: 医疗卫生 | 地区: 上海市 | 推送: 即时</div>
          </div>
          <div class="sub-actions">
            <el-button>编辑</el-button>
            <el-button type="success">启用</el-button>
            <el-button type="danger">删除</el-button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.subscription-view { min-height: 100vh; background: #f5f5f5; }
.header { background: #fff; border-bottom: 1px solid #f0f0f0; position: sticky; top: 0; z-index: 100; }
.header-inner { max-width: 1200px; margin: 0 auto; padding: 0 24px; height: 64px; display: flex; align-items: center; justify-content: space-between; }
.logo { display: flex; align-items: center; gap: 8px; font-size: 20px; font-weight: 600; color: #1890ff; text-decoration: none; }
.logo-icon { width: 32px; height: 32px; background: linear-gradient(135deg, #1890ff, #69c0ff); border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 18px; }
.user-avatar { width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, #1890ff, #69c0ff); display: flex; align-items: center; justify-content: center; color: #fff; font-weight: 600; cursor: pointer; border: 2px solid #faad14; }
.main { max-width: 1200px; margin: 0 auto; padding: 24px; }
.page-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; }
.page-header h2 { font-size: 20px; font-weight: 600; }
.subscription-list { background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); overflow: hidden; }
.subscription-item { display: flex; justify-content: space-between; align-items: center; padding: 20px; border-bottom: 1px solid #f0f0f0; }
.subscription-item:last-child { border-bottom: none; }
.sub-tags { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; }
.sub-detail { font-size: 13px; color: #8c8c8c; }
.sub-actions { display: flex; gap: 8px; }
</style>
