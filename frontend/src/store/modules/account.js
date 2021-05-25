import cookies from 'vue-cookies'

const AccountStore = {
    namespaced: true,
    state: {
        message : 'Store내의 모듈화된 AccountStore 내의 state 값을 가져온다는 뜻을 가진 메세지',
        authToken: cookies.get('auth-token'),
        userData:{
            email:'',
            pw:'',
            nickname:'',
        },
    },
    getters: {
        GET_MESSAGE: state => state.message
    },
    mutations: {
        SET_TOKEN(state, token) {
            state.authToken = token
            cookies.set('auth-token', token)
        },
        SET_USERDATA(state, data){
            state.userData.email = data.email
            state.userData.pw = data.pw
            state.userData.nickname = data.nickname
        },
        REMOVE_TOKEN(state){
            state.authToken = ''
            cookies.remove("auth-token")
        }
    },
    actions: {
        // AC_USER_NAME: ({ commit }, payload) => {
        //     commit('MU_USER_NAME', payload)
        // }
    }
}

export default AccountStore