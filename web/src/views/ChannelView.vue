<script setup>
  import { ref, onMounted } from "vue";
  import { useMessage, useLoadingBar } from "naive-ui";
  import ButtonGroup from "../components/ButtonGroup.vue";
  import { get_listening, get_stats_main } from "../utils/api";


  const listen = ref(0)
  const loading = ref(true)
  const cirLoad = ref(true)
  const isClick = ref(false)
  const message = useMessage()
  const loadLine = useLoadingBar()

  const fetchData = async (configParam = null) => {
    loadLine.start();
    try {
      const [listenData] = await Promise.all([
        get_listening(),
        configParam ? get_stats_main(configParam) : Promise.resolve(null)
      ])
      cirLoad.value = false;
      listen.value = listenData.data.length;
      // message.success("获取数据成功");
    } catch (e) {
      loadLine.error();
      message.error("获取数据失败");
    } finally {
      loadLine.finish();
      loading.value = false;
    }
  }

  const updateButtons = (newButtons) => {buttons.value = newButtons;}
  const handleClick = async (param = null) => {
    isClick.value = !isClick.value;
    await fetchData(param);
  }

  const buttons = ref([
    { id: 6, label: "最近", isClick: true },
    { id: 1, label: "入场", isClick: false },
    { id: 2, label: "收入", isClick: false },
    { id: 3, label: "弹幕", isClick: false },
    { id: 4, label: "上舰", isClick: false }
  ])

  onMounted(() => {
    if (buttons.value[0].isClick) {
      handleClick(buttons.value[0].id);
    } else {
      fetchData();
    }
  })
</script>


<template>
  <div id="head">
    <n-gradient-text :size="50">
      CHANNEL
    </n-gradient-text>
    <p id="bar-title">直播间</p>
    <br />
  </div>
  <br />
  <div style="max-width: 1000px; margin: 0px auto;">
    <n-spin :show="cirLoad">
      <n-card bordered embedded size="small" >
        <n-space vertical justify="center" align="center">
          <ButtonGroup :buttons="buttons" @update:buttons="updateButtons" @button-click="handleClick" />
        </n-space>
      </n-card>
      <n-divider>
        <n-text depth="3">
          共
          <count-to :startVal="0" :endVal="listen" :duration="2000" />
          个直播间
        </n-text>
      </n-divider>
    </n-spin>
  </div>
</template>
