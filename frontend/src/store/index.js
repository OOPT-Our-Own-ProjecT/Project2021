import Vue from 'vue'
import Vuex from 'vuex'

import AccountStore from './modules/account.js'

import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

const store = new Vuex.Store({
    modules: {
        accountStore : AccountStore
    },
    plugins: [
        createPersistedState({
            paths: ["accountStore"] ,
            //모든 state값을 localstorage에 저장할 경우 퍼포먼스의 문제가 발생할 수 있으므로 필요한 모듈만 선택해서 저장하는 것이 좋습니다.
        })
    ],
})

export default store