<template>
    <div>
        <div>
            <NavigationBar></NavigationBar>
        </div>
        <h2>환영합니다. {{userInfo.nickname}} 님!</h2>
        <div>
            <textarea v-model="userInfo.nickname"></textarea>
            <button @click="update()">닉네임 변경</button>
            <button @click="logout()">로그아웃</button>
        </div>
    </div>
</template>

<script>

import NavigationBar from '@/components/navigationBar.vue'
import {updateUser} from '@/api/index';
import {mapState, mapMutations} from 'vuex'

const accountStore = 'accountStore'

export default {
    components:{
        NavigationBar
    },

    computed: {
        ...mapState(accountStore,["authToken" , "userData"]),
    },


	data () {
		return {
            userInfo: {
                email: '',
                pw: '',
                nickname: ''
            },
            token: '',
        }
    },
    created(){
        this.userInfo.email = this.userData.email
        this.userInfo.pw = this.userData.pw
        this.userInfo.nickname = this.userData.nickname
        this.token = this.authToken
    },
    methods: {
        ...mapMutations(accountStore, [
                'REMOVE_TOKEN'
        ]),

        async update(){
                const userData = {
                    email: this.userInfo.email,
                    nickname: this.userInfo.nickname,
                };
                const{ data } = await updateUser(userData);
                alert(data.message)
                this.logout()
        },
        logout(){
            alert("로그아웃 합니다.")
            this.REMOVE_TOKEN()
            this.$router.push('/')
        },
    },
}
</script>

<style>

</style>