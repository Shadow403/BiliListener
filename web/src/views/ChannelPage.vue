<script setup>
  import { useRoute } from 'vue-router';
  import { ref, onMounted, computed, h } from "vue";
  import { 
    useMessage, 
    useLoadingBar, 
    NTooltip, NTag, 
    NSpace, 
    NStatistic 
  } from "naive-ui";
  import { ArrowBackCircleSharp } from '@vicons/ionicons5';
  import { Home16Filled, Live24Regular } from '@vicons/fluent'

  import { get_config_by_uid } from '../utils/api';

  const route = useRoute();
  const message = useMessage();
  const loadBar = useLoadingBar();
  const userUID = computed(() => route.params.uid);

  const columns = ref([])
  const loading = ref(true);
  const live_config = ref(null);

  const fetchData = async (configParam = null) => {
    loadBar.start();
    try {
      const [ret_config] = await Promise.all([
        configParam ? get_config_by_uid(configParam) : Promise.resolve(null)
      ]);

      if (ret_config && ret_config.code === 0) {
        live_config.value = ret_config.data;
      } else {
        message.error('无该 UID 记录');
      }
    } catch (error) {
      console.error('[Fetch Error]: ', error);
      loadBar.error();
      message.error('获取数据失败');
    } finally {
      loadBar.finish();
      columns.value = createColumns(live_config.value);
      loading.value = false;
    }
  };

  onMounted(() => {
    if (userUID.value) {
      fetchData(userUID.value);
    } else {
      message.error('INVALID UID');
    }
  });

  function createColumns(configParam) {
    return [{title() {
          return h(NSpace,{
              justify: "center",
              align: "center"
            },{
              default: () => [
                h(NTag,{
                    size: 'small',
                    type: 'success'
                  },
                  { default: () => `${configParam.live_count} 条` }
                ),
                h(NStatistic,{
                    'tabular-nums': true,
                    label: 'small',
                    value: '1',
                  }
                ),
              ]
            }
          );
        }
      },
    ];
  }

  const data = [
    {
        "uid": 3742241,
        "uuid": "af44505c-0981-5087-8900-3b6d93500160",
        "name": "永远长不大的晓雨",
        "live_time": 1734775259,
        "live_title": "香软可爱男孩~",
        "live_cover_url": "https://i0.hdslb.com/bfs/live/new_room_cover/29586ec49ea79052c495cbfa38c72099eaeba3c5.jpg",
        "live_area": 6,
        "live_area_name": "生活娱乐",
        "live_area_v2_id": 851,
        "live_area_v2_name": "虚拟男V",
        "live_area_v2_parent_id": 9,
        "live_area_v2_parent_name": "虚拟主播",
        "live_tags": "小男孩,弟弟音,少年音,单机游戏,虚拟主播,可爱,整活,猫耳,情感",
        "live_tags_name": "日常,学习,萌宠,厨艺,手机直播",
        "if_full": true,
        "is_finished": true,
        "all_gift": {
            "all": 14,
            "gold": null,
            "silver": null
        },
        "all_price": null,
        "all_enter": 557,
        "all_guard": 2,
        "all_danmaku": 1471,
        "all_superchat": 0,
        "start_timestamp": 1734765450,
        "end_timestamp": 1734797449
    },
    {
        "uid": 3742241,
        "uuid": "9b8b4344-82b5-5896-bc86-bdfc992c64e5",
        "name": "永远长不大的晓雨",
        "live_time": 1735475561,
        "live_title": "香软可爱男孩~",
        "live_cover_url": "https://i0.hdslb.com/bfs/live/new_room_cover/29586ec49ea79052c495cbfa38c72099eaeba3c5.jpg",
        "live_area": 6,
        "live_area_name": "生活娱乐",
        "live_area_v2_id": 851,
        "live_area_v2_name": "虚拟男V",
        "live_area_v2_parent_id": 9,
        "live_area_v2_parent_name": "虚拟主播",
        "live_tags": "小男孩,弟弟音,少年音,单机游戏,虚拟主播,可爱,整活,猫耳,情感",
        "live_tags_name": "日常,学习,萌宠,厨艺,手机直播",
        "if_full": true,
        "is_finished": true,
        "all_gift": {
            "all": 39,
            "gold": null,
            "silver": null
        },
        "all_price": null,
        "all_enter": 317,
        "all_guard": 1,
        "all_danmaku": 1550,
        "all_superchat": 0,
        "start_timestamp": 1735367448,
        "end_timestamp": 1735488457
    }
  ];


</script>


<template>
  <div>
    <div id="head">
        <n-gradient-text :size="50">
        CHANNEL
        </n-gradient-text>
        <p id="bar-title">直播间</p>
        <br />
    </div>
    <br />
    <div style="max-width: 1000px; justify-content: center; margin: 0px auto;">
      <n-card bordered embedde>
        <template #header>
          <n-button size="tiny" secondary circle>
            <n-icon size="25">
              <ArrowBackCircleSharp />
            </n-icon>
          </n-button>
        </template>
        <div style="text-align: center;">
          <n-space vertical justify="center" align="center" style="gap: 5px;">
            <n-avatar
              round
              :size="64"
              src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
            />
            <n-space justify="center" align="center" style="font-size: 24px;">
              <n-tag :bordered="false" type="info">
                Example
              </n-tag>
              NAME
            </n-space>
            <n-text depth="3">
              UID
            </n-text>
          </n-space>
          <br />
          <n-button-group>
            <n-tooltip trigger="hover">
              <template #trigger>
                <n-button ghost size="small">
                  <template #icon>
                    <n-icon><Home16Filled /></n-icon>
                  </template>
                </n-button>
              </template>
              主页
            </n-tooltip>
            <n-tooltip trigger="hover">
              <template #trigger>
                <n-button ghost size="small">
                  <template #icon>
                    <n-icon><Live24Regular /></n-icon>
                  </template>
                </n-button>
              </template>
              直播间
            </n-tooltip>
          </n-button-group>
        </div>
      </n-card>
      <br />
      <br />
      <n-data-table :columns="columns" :data="data" />
    </div>
  </div>
</template>

<style scoped>
:deep(.back) {
  font-size: 17px;
  font-weight: 500;
}
</style>
