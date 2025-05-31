// frontend/vite.config.ts
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';      // ← 추가
import path from 'path';

export default defineConfig({
  plugins: [
    vue(),                                 // ← 등록
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
});
