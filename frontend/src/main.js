import Vue from 'vue'
import App from './App.vue'

import store from './store/index.js'
//store 사용.
import router from './router'
//router 사용.
import VueSession from 'vue-session'
//vue session 사용.

Vue.config.productionTip = false

var sessionOptions = {
  persist: true
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

Vue.use(VueSession, sessionOptions)