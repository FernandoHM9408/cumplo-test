import Vue from 'vue'
import Vuex from 'vuex'
import axios from '@/api';

Vue.use(Vuex)

const state = {
  data: null,
};

const actions = {
  getCurrencyData({ commit }, data) {
    return new Promise((resolve, reject) => {
      axios.get(`api/series/currency/${data.currency}/${data.init_date}/${data.end_date}`, )
        .then((res) => {
          commit('setCurrencyData', res.data);
          resolve(res.data);
        })
        .catch((err) => { reject(err) });
    });
  },
};

const mutations = {
  setCurrencyData(data) {
    state.data = data;
  },
};


const store = new Vuex.Store({
  strict: true,
  state: state,
  mutations: mutations,
  actions: actions,
})

export default store
