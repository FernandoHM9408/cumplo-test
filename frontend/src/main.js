import Vue from 'vue'
import store from '@/store'
import router from '@/router'

import 'bulma/css/bulma.css';
import 'bulma-calendar/dist/css/bulma-calendar.min.css';

import axios from 'axios'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'


import App from '@/App.vue'
import './registerServiceWorker'

Vue.config.productionTip = false

require('../public/css/main.scss');

new Vue({
  router,
  store,

  render: h => h(App)
}).$mount('#app')
