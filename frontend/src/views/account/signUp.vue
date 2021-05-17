<template>
    <div>
        <strong>회원가입 페이지</strong>
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