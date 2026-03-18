<template>
  <div class="detail-view">
    <header class="header">
      <div class="header-inner">
        <div class="logo">
          <div class="logo-icon">📋</div>
          <span>招标头条</span>
        </div>
        <div class="header-search">
          <input type="text" placeholder="搜索招标、中标、项目..." />
          <button>搜索</button>
        </div>
        <div class="header-actions">
          <div class="user-avatar">张</div>
        </div>
      </div>
    </header>

    <main class="main">
      <div class="breadcrumb">
        <router-link to="/">首页</router-link> > <router-link to="/list">招标信息</router-link> > <span>详情</span>
      </div>

      <div class="detail-content">
        <div class="detail-header">
          <el-tag type="primary">招标公告</el-tag>
          <div class="detail-actions">
            <el-button text><el-icon><Star /></el-icon> 收藏</el-button>
            <el-button text><el-icon><Share /></el-icon> 分享</el-button>
            <el-button text><el-icon><Printer /></el-icon> 打印</el-button>
          </div>
        </div>

        <h1 class="detail-title">杭州市某区政务服务中心信息化建设项目公开招标公告</h1>

        <div class="detail-info">
          <div class="info-item"><span class="label">项目编号：</span>HZCG-2026-0317</div>
          <div class="info-item"><span class="label">项目预算：</span>¥ 1,200,000.00 元</div>
          <div class="info-item"><span class="label">招标人：</span>杭州市某区政务服务中心</div>
          <div class="info-item"><span class="label">代理机构：</span>XX招标代理有限公司</div>
          <div class="info-item"><span class="label">发布时间：</span>2026-03-17</div>
          <div class="info-item"><span class="label">报名截止：</span>2026-04-01</div>
          <div class="info-item"><span class="label">地区：</span>浙江省</div>
          <div class="info-item"><span class="label">行业：</span>政府采购</div>
        </div>

        <el-tabs v-model="activeTab" class="detail-tabs">
          <el-tab-pane label="基本信息" name="basic">
            <div class="tab-content">
              <h3>招标公告正文</h3>
              <p>根据《中华人民共和国政府采购法》等有关规定，现对杭州市某区政务服务中心信息化建设项目进行公开招标，欢迎合格的供应商前来投标。</p>
              <h4>一、项目基本情况</h4>
              <p>项目名称：杭州市某区政务服务中心信息化建设项目</p>
              <p>预算金额：¥1,200,000.00元</p>
              <p>采购需求：详见招标文件</p>
              <h4>二、申请人的资格要求</h4>
              <p>1. 具有独立承担民事责任的能力；</p>
              <p>2. 具有良好的商业信誉和健全的财务会计制度；</p>
              <p>3. 具有履行合同所必需的设备和专业技术能力；</p>
              <p>4. 有依法缴纳税收和社会保障资金的良好记录。</p>
            </div>
          </el-tab-pane>
          <el-tab-pane label="招标内容" name="content">
            <div class="tab-content">
              <p>详细内容见附件招标文件</p>
            </div>
          </el-tab-pane>
          <el-tab-pane label="附件下载" name="files">
            <div class="tab-content">
              <div class="file-list">
                <div class="file-item">📄 招标文件.pdf</div>
                <div class="file-item">📄 技术要求.docx</div>
              </div>
            </div>
          </el-tab-pane>
        </el-tabs>

        <div class="vip-lock" v-if="!isVip">
          <div class="lock-icon">🔒</div>
          <div class="lock-text">查看完整信息并下载附件</div>
          <el-button type="warning" size="large">开通VIP会员</el-button>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Star, Share, Printer } from '@element-plus/icons-vue'

const activeTab = ref('basic')
const isVip = ref(true)
</script>

<style scoped>
.detail-view { min-height: 100vh; background: #f5f5f5; }
.header { background: #fff; border-bottom: 1px solid #f0f0f0; position: sticky; top: 0; z-index: 100; }
.header-inner { max-width: 1400px; margin: 0 auto; padding: 0 24px; height: 64px; display: flex; align-items: center; justify-content: space-between; }
.logo { display: flex; align-items: center; gap: 8px; font-size: 20px; font-weight: 600; color: #1890ff; }
.logo-icon { width: 32px; height: 32px; background: linear-gradient(135deg, #1890ff, #69c0ff); border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 18px; }
.header-search { flex: 1; max-width: 600px; margin: 0 32px; display: flex; }
.header-search input { flex: 1; padding: 0 12px; border: 1px solid #d9d9d9; font-size: 14px; outline: none; }
.header-search button { padding: 0 20px; background: #1890ff; border: none; color: #fff; font-size: 14px; cursor: pointer; }
.header-actions { display: flex; align-items: center; gap: 16px; }
.user-avatar { width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, #1890ff, #69c0ff); display: flex; align-items: center; justify-content: center; color: #fff; font-weight: 600; cursor: pointer; border: 2px solid #faad14; }
.main { max-width: 1200px; margin: 0 auto; padding: 24px; }
.breadcrumb { margin-bottom: 16px; color: #8c8c8c; }
.breadcrumb a { color: #1890ff; text-decoration: none; }
.breadcrumb span { color: #262626; }
.detail-content { background: #fff; border-radius: 8px; padding: 24px; }
.detail-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }
.detail-actions { display: flex; gap: 8px; }
.detail-title { font-size: 24px; font-weight: 600; margin-bottom: 20px; line-height: 1.5; }
.detail-info { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; padding: 20px; background: #fafafa; border-radius: 8px; margin-bottom: 24px; }
.info-item { font-size: 14px; }
.info-item .label { color: #8c8c8c; }
.detail-tabs { margin-bottom: 24px; }
.tab-content { padding: 20px 0; line-height: 2; }
.tab-content h3 { margin-bottom: 16px; }
.tab-content h4 { margin: 16px 0 8px; }
.file-list { display: flex; flex-direction: column; gap: 12px; }
.file-item { padding: 12px; background: #f5f5f5; border-radius: 4px; cursor: pointer; }
.file-item:hover { background: #e6f7ff; }
.vip-lock { text-align: center; padding: 40px; background: linear-gradient(135deg, #fffbe6, #fff); border: 1px solid #ffe58f; border-radius: 8px; }
.lock-icon { font-size: 48px; margin-bottom: 16px; }
.lock-text { font-size: 16px; color: #595959; margin-bottom: 20px; }
</style>
