// frontend/src/main.ts
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router';    // ← 추가된 부분

const app = createApp(App);
app.use(createPinia());
app.use(router);                 // ← 라우터 등록
app.mount('#app');
