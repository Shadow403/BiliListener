<script>
import { darkTheme } from "naive-ui";
import { defineComponent, onMounted, provide, ref } from "vue";
import { Home16Filled, Live24Regular, Search20Filled, Info24Filled } from '@vicons/fluent'

export default defineComponent({
  components: {
    Home16Filled,
    Live24Regular,
    Search20Filled,
    Info24Filled
  },
  setup() {
    const theme = ref(darkTheme);

    provide('theme', theme);

    onMounted(() => {
      const storedTheme = localStorage.getItem('theme');
      if (storedTheme) {
        theme.value = storedTheme === 'dark' ? darkTheme : null;
      }
    });
    return {
      theme
    };
  }});
</script>


<template>
  <n-config-provider :theme="theme">
    <n-loading-bar-provider>
    <n-message-provider>
    <n-layout position="static" id="n-layout-static">
      <n-layout-header bordered>
        <n-space>
          <router-link to="/" tag="n-button">
            <n-button text tag="index" href="/">
              <template #icon>
                <n-icon>
                  <Home16Filled />
                </n-icon>
              </template>
              主页
            </n-button>
          </router-link>
          <router-link to="/channel" tag="n-button">
            <n-button text tag="channel">
              <template #icon>
                <n-icon>
                  <Live24Regular />
                </n-icon>
              </template>
              直播间
            </n-button>
          </router-link>
          <router-link to="/search" tag="n-button">
            <n-button text tag="search">
              <template #icon>
                <n-icon>
                  <Search20Filled />
                </n-icon>
              </template>
              查询
            </n-button>
          </router-link>
          <router-link to="/about" tag="n-button">
            <n-button text tag="about">
              <template #icon>
                <n-icon>
                  <Info24Filled />
                </n-icon>
              </template>
              关于
            </n-button>
          </router-link>
        </n-space>
      </n-layout-header>
    </n-layout>
    <n-layout position="absolute" id="n-layout-absolute">
      <n-scrollbar content-style="padding: 12px;">
        <!--  -->
        <RouterView />
        <!--  -->
      </n-scrollbar>
    </n-layout>
    </n-message-provider>
    </n-loading-bar-provider>
    <n-global-style />
  </n-config-provider>
</template>

<style scoped>
#n-layout-static {
  height: 100vh;
}

#n-layout-absolute {
  height: calc(-50px + 100vh);
  top: 50px;
}

.n-layout-header {
  height: 50px;
  display: flex;
  align-items: flex-end;
  justify-content: center;
}

.n-space {
  display: flex;
  flex-flow: wrap;
  justify-content: center;
  gap: 8px 12px;
  padding-bottom: 7px
}
</style>

