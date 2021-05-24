const AccountStore = {
    namespaced: true,
    state: {
        message : 'Store내의 모듈화된 AccountStore 내의 state 값을 가져온다는 뜻을 가진 메세지'
    },
    getters: {
        GET_MESSAGE: state => state.message
    },
    mutations: {
        // MU_USER_NAME: (state, payload) => {
        //     /*
        //         여기서는 payload를 객체로 받습니다.
        //         payload를 객체로 받으면, mutation를 조금더 유연하게 사용할 수 있기는 합니다.
        //     */
        //     state.userName = payload.userName
        // }
    },
    actions: {
        // AC_USER_NAME: ({ commit }, payload) => {
        //     commit('MU_USER_NAME', payload)
        // }
    }
}

export default AccountStore