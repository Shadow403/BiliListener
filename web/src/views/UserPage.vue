<script setup>
  import { ref, onMounted, computed } from "vue";
  import { useMessage, useLoadingBar } from "naive-ui";
  import { get_config_by_uid } from '../utils/api';
  import { useRoute } from 'vue-router';

  const message = useMessage();
  const loadingBar = useLoadingBar();
  const show = ref(true);
  const loading = ref(true);
  const live_config = ref(null);

  const route = useRoute();
  const userId = computed(() => route.params.uid);

  const fetchData = async (configParam = null) => {
    loadingBar.start();
    try {
      const [ret_config] = await Promise.all([
        configParam ? get_config_by_uid(configParam) : Promise.resolve(null)
      ]);

      if (ret_config && ret_config.code === 0) {
        show.value = false;
        live_config.value = ret_config.data;
      } else {
        message.error('无该 UID 记录');
      }
    } catch (error) {
      console.error('[Fetch Error]: ', error);
      loadingBar.error();
      message.error('获取数据失败');
    } finally {
      loadingBar.finish();
      loading.value = false;
    }
  };

  onMounted(() => {
    if (userId.value) {
      fetchData(userId.value);
    } else {
      fetchData();
    }
  });
</script>


<template>

</template>
