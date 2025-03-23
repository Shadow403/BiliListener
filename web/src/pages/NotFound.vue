<script setup>
  const mainpage = () => {
    window.location.href = '/'
  }

</script>

<template>
  <n-result status="404" title="404 资源不存在" description="又到处乱逛">
    <template #footer>
    <n-button @click="mainpage">返回主页</n-button>
    </template>
  </n-result>
</template>
