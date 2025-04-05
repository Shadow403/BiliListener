import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

const env = process.env.NODE_ENV
const ws_api = env === 'production' ? 'ws://ws-blistener.shadow403.cn' : 'ws://127.0.0.1:5700'
const http_api = env === 'production' ? 'https://api-blistener.shadow403.cn/api' : 'http://127.0.0.1:5700/api'

export default defineConfig({
  define: {
    'import.meta.env.VITE_WS_API': JSON.stringify(ws_api),
    'import.meta.env.VITE_HTTP_API': JSON.stringify(http_api)
  },
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
      }
    },
  },
})
