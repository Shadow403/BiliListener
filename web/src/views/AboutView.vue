<script setup>
  import { ref, inject } from "vue";
  import { Api } from '@vicons/carbon';
  import { darkTheme } from "naive-ui";
  import { Vuejs, Python } from '@vicons/fa';

  import ButtonGroup from '../components/ButtonGroup.vue';

  const onclickRepo = () => {
    window.open("https://github.com/Shadow403/BiliListener");
  };

  const onclickDanmakus = () => {
    window.open("https://danmakus.com/");
  };

  const onclickAPI = () => {
    window.open("https://bililistener.shadow403.com.cn/");
  };

  const onclickPython = () => {
    window.open("https://www.python.org/");
  };

  const onclickVue3 = () => {
    window.open("https://v3.cn.vuejs.org/");
  };

  const theme = inject('theme');

  const buttons = ref([
    { id: 1, label: 'LIGHT', isClicked: false },
    { id: 2, label: 'DARK', isClicked: false },
  ]);

  const updateButtons = (newButtons) => {
    buttons.value = newButtons;
  };

  const handleButtonClick = (id) => {
    if (id === 1) {
      theme.value = null;
      localStorage.setItem('theme', 'light');
    }
    if (id === 2) {
      theme.value = darkTheme;
      localStorage.setItem('theme', 'dark');
    }
  };
</script>


<template>
  <div id="head">
    <n-gradient-text :size="50">
      ABOUT
    </n-gradient-text>
    <p id="bar-title">关于</p>
    <br />
  </div>

  <div style="max-width: 1000px; margin: 0px auto;">
    <n-card bordered embedded>
      <n-space vertical justify="center" align="center">
        <n-button type="primary">
          添加主播
        </n-button>
        <n-button-group>
          <!-- <n-button ghost @click="autoTheme">LIGHT</n-button> // TODO -->
          <ButtonGroup :buttons="buttons" @update:buttons="updateButtons" @button-click="handleButtonClick" />
        </n-button-group>
      </n-space>
    </n-card>
    <br />
    <p style="text-align: center;">
      <n-gradient-text :size="24" type="success">
        友链
      </n-gradient-text>
    </p>
    <br />
    <n-card bordered embedded>
      <n-list hoverable clickable bordered>
        <n-list-item @click="onclickDanmakus">
          <template #prefix>
            <n-avatar
              size="large"
              src="https://danmakus.com/favicon.ico"
            />
          </template>
          <n-thing 
            title="Danmakus" 
            description="前端设计借鉴于此" 
            title-extra="⌨️"
          />
          https://danmakus.com/
        </n-list-item>
      </n-list>
    </n-card>
    <br />
    <p style="text-align: center;">
      <n-gradient-text :size="24" type="success">
        仓库
      </n-gradient-text>
    </p>
    <br />
    <n-card bordered embedded>
      <n-list hoverable clickable bordered>
        <n-list-item @click="onclickRepo">
          <template #prefix>
            <n-avatar
              size="large"
              src="https://github.githubassets.com/assets/mona-loading-dark-7701a7b97370.gif"
            />
            <!-- src="./images/repo_cat.png" -->
          </template>
          <n-thing 
            title="REPO" 
            description="https://github.com/Shadow403/BiliListener" 
            title-extra="📦"
          />
        </n-list-item>
      </n-list>
    </n-card>
    <br />
    <br />
    <br />
    <br />
    <n-card bordered embedded>
      <n-space vertical justify="center" align="center">
        <n-space>
          <n-tag :bordered="false">
            <n-button text @click="onclickAPI">API</n-button>
            <template #icon>
              <n-icon :component="Api" />
            </template>
          </n-tag>
        </n-space>
        <n-text type="error" depth="3">禁止用于一切商业行为 😡</n-text>
        <n-text>数据随意使用, 标明来源即可 😋</n-text>
        <n-text depth="3">MADE WITH ❤️ BY
          <n-tooltip trigger="hover">
            <template #trigger>
              <n-text depth="3"> SHADOW403</n-text>
            </template>
            Author
          </n-tooltip>
        </n-text>
        <n-space justify="center" align="center">
          <n-text>⚡ 由</n-text>
          <n-tag :bordered="false">
            <n-button text @click="onclickPython">Python</n-button>
            <template #avatar>
              <n-avatar
                src="https://www.python.org/favicon.ico"
              />
            </template>
            <!-- <template #icon>
              <n-icon :component="Python" />
            </template> -->
          </n-tag>
          <n-text>&</n-text>
          <n-tag :bordered="false">
            <n-button text @click="onclickVue3">VUE 3</n-button>
            <template #avatar>
              <n-avatar
                src="https://cn.vuejs.org/logo.svg"
              />
            </template>
            <!-- <template #icon>
              <n-icon :component="Vuejs" />
            </template> -->
          </n-tag>
          <n-text>驱动 ⚡</n-text>
        </n-space>
      </n-space>
    </n-card>
  </div>
</template>

<style>


</style>
