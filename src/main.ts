import { createApp } from 'vue'
import { createPinia } from 'pinia'

import './assets/css/main.css'
import App from './App.vue'
import { Icon } from "@iconify/vue";
//import router from './router'

const app = createApp(App)
app.component('Icon', Icon); // ignore eslint rule vue/multi-word-component-names

app.use(createPinia())
//app.use(router)

app.mount('#app')
