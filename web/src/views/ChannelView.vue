<script setup>
  import { ref, onMounted } from "vue";
  import { useMessage, useLoadingBar } from "naive-ui";
  import ButtonGroup from '../components/ButtonGroup.vue';
  import { get_listening, get_stats_main } from '../utils/api';

  const startVal = ref(0)
  const duration = ref(2000)

  const listening = ref(0)

  const show = ref(true)
  const loading = ref(true)
  const isClicked = ref(false)

  const message = useMessage()
  const loadLine = useLoadingBar()

  const fetchData = async (configParam = null) => {
    loadLine.start();
    try {
      const [ret_listening] = await Promise.all([
        get_listening(),
        configParam ? get_stats_main(configParam) : Promise.resolve(null)
      ])

      show.value = false;
      listening.value = ret_listening.data.length;
      message.success('获取数据成功');
    } catch (e) {
      console.log(e);
      message.error('获取数据失败');
      loadLine.error();
    } finally {
      loadLine.finish();
      loading.value = false;
    }
  }

  onMounted(() => {
    fetchData();
  })

  const handleClick = async (param = null) => {
    isClicked.value = !isClicked.value;
    await fetchData(param);
  }

  const buttons = ref([
    { id: 1, label: '入场', isClicked: false },
    { id: 2, label: '收入', isClicked: false },
    { id: 3, label: '弹幕', isClicked: false },
    { id: 4, label: '上舰', isClicked: false },
    { id: 6, label: '最近', isClicked: false }
  ])

  const updateButtons = (newButtons) => {
    buttons.value = newButtons;
  }
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
    <n-spin :show="show">
      <n-card bordered embedded size="small" >
        <template #header-title>
          123
        </template>
        <n-space vertical justify="center" align="center">
          <ButtonGroup :buttons="buttons" @update:buttons="updateButtons" @button-click="handleClick" />
          <!-- <ButtonGroup :buttons="buttons" :defaultButtonId="defaultId" @update:buttons="updateButtons" @button-click="handleClick" /> -->
        </n-space>
      </n-card>
      <n-divider>
        <n-text depth="3">
          共
          <count-to :startVal="startVal" :endVal="listening" :duration="duration" />
          个直播间
        </n-text>
      </n-divider>
    </n-spin>
  </div>
</template>
