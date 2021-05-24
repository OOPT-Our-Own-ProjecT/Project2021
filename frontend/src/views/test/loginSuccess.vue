<template>
    <div>
        <div>
            <NavigationBar></NavigationBar>
        </div>
        <h2>환영합니다. {{$session.get('user_nickname')}} 님!</h2>
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

export default {
    components:{
        NavigationBar
    },

	data () {
		return {
            userInfo:{
                nickname: this.$session.get('user_nickname') ,
            }
        }
    },
    methods: {
        async update(){
                const userData = {
                    email: this.$session.get('user_email'),
                    nickname: this.userInfo.nickname,
                };
                const{ data } = await updateUser(userData);
                alert(data.message)
                this.logout()
        },
        logout(){
            alert("로그아웃 합니다.")
            this.$session.destroy()
            this.$router.push('/')
        },
    },
}
</script>

<style>

</style>