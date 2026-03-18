<template>
  <div class="vip-view">
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
      <!-- VIP User Card -->
      <div class="vip-card">
        <div class="vip-info">
          <div class="avatar">张</div>
          <div class="info">
            <div class="greeting">尊敬的用户您好</div>
            <div class="vip-level">您是：年度VIP会员</div>
            <div class="expire">到期时间：2027年3月18日</div>
          </div>
          <el-button type="warning" size="large">续费会员</el-button>
        </div>
      </div>

      <!-- Benefits -->
      <div class="section">
        <h3>VIP专属权益</h3>
        <div class="benefits-grid">
          <div class="benefit-item">
            <div class="benefit-icon">📊</div>
            <div class="benefit-title">无限查看</div>
            <div class="benefit-desc">查看全部招标详细信息</div>
          </div>
          <div class="benefit-item">
            <div class="benefit-icon">📥</div>
            <div class="benefit-title">批量导出</div>
            <div class="benefit-desc">Excel/CSV无限导出</div>
          </div>
          <div class="benefit-item">
            <div class="benefit-icon">🔔</div>
            <div class="benefit-title">优先推送</div>
            <div class="benefit-desc">第一时间推送新标讯</div>
          </div>
          <div class="benefit-item">
            <div class="benefit-icon">🎯</div>
            <div class="benefit-title">竞品分析</div>
            <div class="benefit-desc">中标企业深度分析</div>
          </div>
        </div>
      </div>

      <!-- Pricing -->
      <div class="section">
        <h3>开通/续费</h3>
        <div class="pricing-grid">
          <div class="pricing-item">
            <div class="pricing-title">月度VIP</div>
            <div class="pricing-price">¥99<span>/月</span></div>
            <div class="pricing-desc">适合短期需求</div>
            <el-button style="width: 100%">立即开通</el-button>
          </div>
          <div class="pricing-item featured">
            <div class="featured-tag">省30%</div>
            <div class="pricing-title">年度VIP ⭐</div>
            <div class="pricing-price">¥899<span>/年</span></div>
            <div class="pricing-desc">原价 ¥1188</div>
            <el-button type="warning" style="width: 100%">立即开通</el-button>
          </div>
          <div class="pricing-item">
            <div class="pricing-title">企业版</div>
            <div class="pricing-price">定制</div>
            <div class="pricing-desc">API接口、定制数据</div>
            <el-button style="width: 100%">联系我们</el-button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.vip-view { min-height: 100vh; background: #f5f5f5; }
.header { background: #fff; border-bottom: 1px solid #f0f0f0; position: sticky; top: 0; z-index: 100; }
.header-inner { max-width: 1200px; margin: 0 auto; padding: 0 24px; height: 64px; display: flex; align-items: center; justify-content: space-between; }
.logo { display: flex; align-items: center; gap: 8px; font-size: 20px; font-weight: 600; color: #1890ff; text-decoration: none; }
.logo-icon { width: 32px; height: 32px; background: linear-gradient(135deg, #1890ff, #69c0ff); border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 18px; }
.user-avatar { width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, #1890ff, #69c0ff); display: flex; align-items: center; justify-content: center; color: #fff; font-weight: 600; cursor: pointer; border: 2px solid #faad14; }
.main { max-width: 1200px; margin: 0 auto; padding: 24px; }
.vip-card { background: linear-gradient(135deg, #faad14, #d48806); border-radius: 16px; padding: 32px; color: #fff; margin-bottom: 32px; }
.vip-info { display: flex; align-items: center; gap: 24px; }
.avatar { width: 80px; height: 80px; border-radius: 50%; background: rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; font-size: 32px; border: 3px solid #fff; }
.info { flex: 1; }
.greeting { font-size: 24px; font-weight: 600; margin-bottom: 8px; }
.vip-level { font-size: 16px; opacity: 0.9; margin-bottom: 4px; }
.expire { font-size: 14px; opacity: 0.8; }
.section { background: #fff; border-radius: 12px; padding: 24px; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
.section h3 { font-size: 18px; font-weight: 600; margin-bottom: 20px; }
.benefits-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }
.benefit-item { text-align: center; padding: 20px; }
.benefit-icon { font-size: 32px; margin-bottom: 12px; }
.benefit-title { font-weight: 600; margin-bottom: 4px; }
.benefit-desc { font-size: 12px; color: #8c8c8c; }
.pricing-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
.pricing-item { border: 2px solid #f0f0f0; border-radius: 12px; padding: 24px; text-align: center; cursor: pointer; transition: all 0.2s; position: relative; }
.pricing-item:hover { border-color: #1890ff; }
.pricing-item.featured { border-color: #faad14; }
.featured-tag { position: absolute; top: -12px; left: 50%; transform: translateX(-50%); background: #faad14; color: #fff; padding: 4px 16px; border-radius: 12px; font-size: 12px; }
.pricing-title { font-size: 18px; font-weight: 600; margin-bottom: 12px; }
.pricing-price { font-size: 28px; font-weight: 700; color: #faad14; margin-bottom: 8px; }
.pricing-price span { font-size: 14px; font-weight: 400; color: #8c8c8c; }
.pricing-desc { font-size: 12px; color: #8c8c8c; margin-bottom: 16px; }
</style>
