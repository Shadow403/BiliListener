import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import ChannelView from '../views/ChannelView.vue'
import SearchView from '../views/SearchView.vue'
import UserPage from '../views/UserPage.vue'
import ChannelPage from '../views/ChannelPage.vue'

import NotFound from '../pages/NotFound.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: '主页 · BiliListener',
      component: HomeView,
    },
    {
      path: '/channel',
      name: '直播间 · BiliListener',
      component: ChannelView,
    },
    {
      path: '/search',
      name: '搜索 · BiliListener',
      component: SearchView,
    },
    {
      path: '/about',
      name: '关于 · BiliListener',
      component: AboutView,
    },
    {
      path: '/user/:uid',
      name: '查询 · :uid',
      component: UserPage,
    },
    {
      path: '/channel/:uid',
      name: '直播间 · :uid',
      component: ChannelPage,
    },
    {
      path: '/:catchAll(.*)',
      name: 'NotFound',
      component: NotFound,
    }
  ],
})

export default router
