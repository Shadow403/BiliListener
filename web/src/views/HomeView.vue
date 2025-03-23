<script setup>
  import { ref, onMounted } from "vue"
  import { useMessage, useLoadingBar } from "naive-ui"

  import { get_hub } from '../utils/api'
  import Annoucement from './Announcement.vue'

  const ret_data = ref({
    "time": "",
    "uids": "",
    "live_count": 0,
    "uids_listening": 0,
    "total": {
      "danmaku": 0
    }
  })

  const color = ref('#d03050')
  const blow_id = ref('disable')

  const loading = ref(true)
  const message = useMessage()
  const loadingLine = useLoadingBar()
  const adduid = () => {
    message.info('点这里没用')
  }

  onMounted(async () => {
    loadingLine.start()
    try {
      const response = await get_hub()
      
      color.value = '#18a058'
      blow_id.value = 'enable'
      ret_data.value = response.data
    } catch (e) {
      loadingLine.error();
    } finally {
      loadingLine.finish();
      loading.value = false
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
              {{ ret_data.time }}
            </time>
          </n-space>
        </template>
        <template #header-extra>
          <div>
            <n-badge :color="color" dot :id="blow_id" />
          </div>
        </template>
        <n-skeleton v-if="loading" text :repeat="3" />
          <template v-else>
            <n-space style="display: flex; flex-flow: wrap; justify-content: space-between; gap: 8px 12px;">
              <n-statistic label="收录">
                <count-to :startVal="0" :endVal="ret_data.uids" :duration="2000" />
              </n-statistic>
              <n-statistic label="监听中">
                <count-to :startVal="0" :endVal="ret_data.uids_listening" :duration="2000" />
              </n-statistic>
              <n-statistic label="总场次">
                <count-to :startVal="0" :endVal="ret_data.live_count" :duration="2000" />
              </n-statistic>
              <n-statistic label="总弹幕">
                <count-to :startVal="0" :endVal="ret_data.total.danmaku" :duration="2000" />
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
