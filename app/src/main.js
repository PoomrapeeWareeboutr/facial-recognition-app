import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueCookies from 'vue-cookies'

import 'preline'
import './css/index.css'

createApp(App)
.use(router)
.use(VueCookies)
.mount('#app')
