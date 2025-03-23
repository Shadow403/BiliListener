<script setup>
  import { ref } from "vue"
  import { useRouter } from 'vue-router'
  import { useMessage, useLoadingBar } from "naive-ui"

  import { get_config_by_uid } from '../utils/api'

  const uidInput = ref('')
  const router = useRouter()
  const message = useMessage()
  const loadLine = useLoadingBar()

  const show = ref(true)
  const loading = ref(true)

  const fetchData = async (configParam = null) => {
    loadLine.start()
    try {
      const [ret_config] = await Promise.all([
        configParam ? get_config_by_uid(configParam) : Promise.resolve(null)
      ])

      if (ret_config.code === 0) {
        show.value = false
        router.push(`/user/${configParam}`)
      } else {
        message.error('无该 UID 记录')
      }
    } catch (e) {
      console.error(e)
      message.error('获取数据失败')
      loadLine.error()
    } finally {
      loadLine.finish()
      loading.value = false
    }
  }

  const onclickSearch = () => {
    const uid = uidInput.value
    if (uid) {
      fetchData(uid)
    } else {
      message.error('输入 UID 无效')
    }
  }
</script>


<template>
    <div id="head">
    <n-gradient-text :size="50">
      SEARCH
    </n-gradient-text>
    <p id="bar-title">查询</p>
    <br />
  </div>
  <br />
  <div style="max-width: 1000px; margin: 0px auto;">
    <n-space vertical justify="center">
      <n-card bordered embedded size="small" >
        <n-space vertical justify="center" align="center">
          <n-input-group>
            <n-input-group-label>历史记录</n-input-group-label>
            <n-input v-model:value="uidInput" autofocus placeholder="目标 UID" />
            <n-button @click="onclickSearch">🔍</n-button>
          </n-input-group>
        </n-space>
      </n-card>
    </n-space>
  </div>
</template>

