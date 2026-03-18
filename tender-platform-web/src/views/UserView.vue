<template>
  <div class="user-view">
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
      <div class="user-layout">
        <aside class="sidebar">
          <div class="user-info">
            <div class="avatar">张</div>
            <div class="name">用户</div>
            <div class="vip-tag">年度VIP</div>
          </div>
          <nav class="menu">
            <a class="menu-item active">个人资料</a>
            <a class="menu-item">我的收藏</a>
            <a class="menu-item">浏览历史</a>
            <a class="menu-item">订阅管理</a>
            <a class="menu-item">消息通知</a>
            <a class="menu-item">VIP会员</a>
            <a class="menu-item">设置</a>
          </nav>
        </aside>
        
        <div class="content">
          <h2>个人资料</h2>
          <el-form :model="form" label-width="80px" style="max-width: 500px">
            <el-form-item label="头像">
              <div class="avatar-upload">
                <div class="avatar">张</div>
                <el-button>更换头像</el-button>
              </div>
            </el-form-item>
            <el-form-item label="用户名">
              <el-input v-model="form.username" />
            </el-form-item>
            <el-form-item label="手机号">
              <el-input v-model="form.phone" />
            </el-form-item>
            <el-form-item label="邮箱">
              <el-input v-model="form.email" />
            </el-form-item>
            <el-form-item>
              <el-button type="primary">保存</el-button>
            </el-form-item>
          </el-form>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const form = ref({
  username: '用户',
  phone: '138****8888',
  email: 'user@example.com'
})
</script>

<style scoped>
.user-view { min-height: 100vh; background: #f5f5f5; }
.header { background: #fff; border-bottom: 1px solid #f0f0f0; position: sticky; top: 0; z-index: 100; }
.header-inner { max-width: 1400px; margin: 0 auto; padding: 0 24px; height: 64px; display: flex; align-items: center; justify-content: space-between; }
.logo { display: flex; align-items: center; gap: 8px; font-size: 20px; font-weight: 600; color: #1890ff; text-decoration: none; }
.logo-icon { width: 32px; height: 32px; background: linear-gradient(135deg, #1890ff, #69c0ff); border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 18px; }
.user-avatar { width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, #1890ff, #69c0ff); display: flex; align-items: center; justify-content: center; color: #fff; font-weight: 600; cursor: pointer; border: 2px solid #faad14; }
.main { max-width: 1200px; margin: 0 auto; padding: 24px; }
.user-layout { display: grid; grid-template-columns: 240px 1fr; gap: 24px; }
.sidebar { background: #fff; border-radius: 8px; padding: 24px; }
.user-info { text-align: center; margin-bottom: 24px; padding-bottom: 24px; border-bottom: 1px solid #f0f0f0; }
.avatar { width: 80px; height: 80px; border-radius: 50%; background: linear-gradient(135deg, #1890ff, #69c0ff); display: flex; align-items: center; justify-content: center; color: #fff; font-size: 28px; font-weight: 600; margin: 0 auto 12px; }
.name { font-size: 18px; font-weight: 600; margin-bottom: 8px; }
.vip-tag { display: inline-block; background: linear-gradient(135deg, #faad14, #d48806); color: #fff; padding: 4px 12px; border-radius: 12px; font-size: 12px; }
.menu-item { display: block; padding: 12px 16px; color: #595959; text-decoration: none; border-radius: 6px; margin-bottom: 4px; cursor: pointer; }
.menu-item:hover, .menu-item.active { background: #e6f7ff; color: #1890ff; }
.content { background: #fff; border-radius: 8px; padding: 24px; }
.content h2 { margin-bottom: 24px; }
.avatar-upload { display: flex; align-items: center; gap: 16px; }
</style>
