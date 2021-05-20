<template>
    <div>
        <strong>메인페이지</strong>
        <br><br>
        <div>
          <input placeholder="ID 입력" v-model="userData.id">
          <input type="password" placeholder="비번 입력" v-model="userData.pw">
        </div>
        <br>
        <div>
            <button @click="login">로그인</button>
            <router-link to="/signUp">회원가입</router-link>
        </div>
    </div>
</template>

<script>
    export default {
        data: () => ({
            userData : {
                id : "",
                pw :  "",
            }
        }),

        methods: {
            login(){
                console.log("로그인 메소드 실행")
                console.log(this.userData.id)
                console.log(this.userData.pw)
            }
        },
    }
</script>

<style scoped>
</style>