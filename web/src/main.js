import naive from 'naive-ui'
import countTo from 'vue3-count-to';

import App from './App.vue'
import router from './router'

import 'vfonts/Lato.css'
import './assets/main.css'
import 'vfonts/FiraCode.css'

import { createApp } from 'vue'


const app = createApp(App)

app.use(naive)
app.use(router)
app.use(countTo)

app.mount('#app')
