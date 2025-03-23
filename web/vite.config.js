import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

const ws_api = 'ws://192.168.10.31:5701'
// const http_api = 'http://192.168.10.31:5700/api'
const http_api = 'http://127.0.0.1:5700/api'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  server: {
    proxy: {
      '/api': {
        target: http_api,
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
      '/ws': {
        target: ws_api,
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/ws/, ''),
      }
    },
  },
})
