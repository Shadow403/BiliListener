<script setup>
  import { ref, onMounted, onBeforeUnmount } from "vue"
  import { useMessage, useLoadingBar } from "naive-ui"

  import Annoucement from './Announcement.vue'

  const newinitData = ref({
    "time": "N / A",
    "uids": 0,
    "live_count": 0,
    "uids_listening": 0,
    "total": {
      "enter": 0,
      "danmaku": 0
    }
  })

  let socket = null
  const loading = ref(true)
  const message = useMessage()
  const loadLine = useLoadingBar()
  const countToDuration = ref(2000)
  const breathLight = ref("disable")
  const breathColor = ref("#D03050")
  const oldInitData = ref(newinitData.value)
  const adduid = () => {message.info('点这里没用')}

  onMounted(async () => {
    loadLine.start()
    const wsUrl = import.meta.env.VITE_WS_API + "/v1/ws/hub"
    if (!socket) {
      socket = new WebSocket(wsUrl)
      socket.onmessage = (event) => {
        const data = JSON.parse(event.data)
        oldInitData.value = { ...newinitData.value }
        newinitData.value = data.data
        breathLight.value = "enable"
        breathColor.value = "#18A058"
        loadLine.finish();
        loading.value = false
      }
      socket.onerror = (e) => {
        loadLine.error();
        loading.value = true
        message.error("连接失败")
      }
    }
  })

  onBeforeUnmount(() => {
    if (socket) {
      socket.close()
      socket = null
    }
  })
</script>



<template>
  <div>
    <div style="text-align: center;">
      <p style="font-size: 7vw; font-weight: 750;">
        <n-gradient-text id="title">
          BILILISTENER
        </n-gradient-text>
      </p>
      <n-gradient-text id="bar-title">
        弹幕站
      </n-gradient-text>
      <br>
      <br>
    </div>
    <div style="max-width: 1000px; margin: auto;">
      <n-card bordered embedded>
        <template #header>
          <n-space>
            数据
            <time>
              {{ newinitData.time }}
            </time>
          </n-space>
        </template>
        <template #header-extra>
          <div>
            <n-badge :color="breathColor" dot :id="breathLight" />
          </div>
        </template>
        <n-skeleton v-if="loading" text :repeat="3" />
          <template v-else>
            <n-space style="display: flex; flex-flow: wrap; justify-content: space-between; gap: 8px 12px;">
              <n-statistic label="收录">
                <count-to :startVal="oldInitData.uids" :endVal="newinitData.uids" :duration="countToDuration" />
              </n-statistic>
              <n-statistic label="监听中">
                <count-to :startVal="oldInitData.uids_listening" :endVal="newinitData.uids_listening" :duration="countToDuration" />
              </n-statistic>
              <n-statistic label="总场次">
                <count-to :startVal="oldInitData.live_count" :endVal="newinitData.live_count" :duration="countToDuration" />
              </n-statistic>
              <n-statistic label="总入场">
                <count-to :startVal="oldInitData.total.enter" :endVal="newinitData.total.enter" :duration="countToDuration" />
              </n-statistic>
              <n-statistic label="总弹幕">
                <count-to :startVal="oldInitData.total.danmaku" :endVal="newinitData.total.danmaku" :duration="countToDuration" />
              </n-statistic>
            </n-space>
          </template>
          <n-divider />
          <n-collapse :default-expanded-names="['1']">
            <n-collapse-item name="1" title="使用">
              <n-h2 prefix="bar">
                <n-text type="primary">
                  😕 怎么用?
                </n-text>
              </n-h2>
              <n-text italic depth="3">
                以下是基本用法 🙌
              </n-text>
              <n-collapse-item name="2" title="添加主播 😍">
                <n-ul>
                  <n-li>点击最上方导航栏最后一个, 即 
                    <n-text type="info">
                      <a href="/about">关于</a>
                    </n-text>
                  </n-li>
                  <n-li>稍微往下拉一点有个 
                    <n-button strong secondary type="success" @click="adduid">
                      添加主播
                    </n-button>
                  </n-li>
                  <n-li>点击之后输入用户
                    <n-text type="info">uid</n-text>
                      就是了
                    </n-li>
                </n-ul>
              </n-collapse-item>
              <n-collapse-item name="3" title="用户历史记录 🤓">
                <n-ul>
                  <n-li>点击最上方导航栏第四个, 即 
                    <n-text type="info">
                      <a href="/search">查询</a>
                    </n-text>
                  </n-li>
                  <n-li>历史记录当然只有监听到的数据 😢</n-li>
                </n-ul>
              </n-collapse-item>
            </n-collapse-item>
            <n-divider />
            <n-h2 prefix="bar" type="error">
              <n-text type="error">
                这里是公告 📢
              </n-text>
              </n-h2>
              <!--  -->
              <Annoucement />
              <!--  -->
          </n-collapse>
      </n-card>
    </div>
  </div>
</template>


<style scoped>
#title {
  font-weight: 500;
}

#bar-title {
  background-image: linear-gradient(0deg, rgb(171, 171, 171) 0%, rgb(170, 170, 170) 100%);
  font-size: 20px;
}

#enable {
  animation: 2.5s ease 0s infinite normal none running animated-border-round;
}

</style>
