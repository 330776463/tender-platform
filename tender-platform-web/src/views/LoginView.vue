<template>
  <div class="login-view">
    <div class="login-box">
      <div class="login-header">
        <div class="logo-icon">📋</div>
        <h1>招标头条</h1>
      </div>
      
      <el-form :model="form" class="login-form">
        <el-form-item>
          <el-input v-model="form.phone" placeholder="手机号" size="large">
            <template #prefix><el-icon><User /></el-icon></template>
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-input v-model="form.code" placeholder="验证码" size="large" style="width: 60%">
            <template #prefix><el-icon><Lock /></el-icon></template>
          </el-input>
          <el-button size="large" style="width: 38%; margin-left: 2%">获取验证码</el-button>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" size="large" style="width: 100%">登录</el-button>
        </el-form-item>
      </el-form>
      
      <div class="login-footer">
        <span>还没有账号？</span>
        <el-link type="primary">立即注册</el-link>
      </div>
      
      <div class="wechat-login">
        <el-divider>其他登录方式</el-divider>
        <div class="wechat-btn">💬 微信登录</div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { User, Lock } from '@element-plus/icons-vue'

const form = ref({
  phone: '',
  code: ''
})
</script>

<style scoped>
.login-view { min-height: 100vh; display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, #e6f7ff 0%, #fff 100%); }
.login-box { width: 400px; padding: 40px; background: #fff; border-radius: 12px; box-shadow: 0 6px 16px rgba(0,0,0,0.12); }
.login-header { text-align: center; margin-bottom: 32px; }
.logo-icon { width: 64px; height: 64px; background: linear-gradient(135deg, #1890ff, #69c0ff); border-radius: 16px; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 32px; margin: 0 auto 16px; }
.login-header h1 { font-size: 24px; color: #1890ff; }
.login-form { margin-bottom: 16px; }
.login-footer { text-align: center; }
.login-footer span { color: #8c8c8c; }
.wechat-login { margin-top: 24px; }
.wechat-btn { text-align: center; padding: 12px; border: 1px solid #d9d9d9; border-radius: 6px; cursor: pointer; }
.wechat-btn:hover { border-color: #52c41a; color: #52c41a; }
</style>
