<template>
    <div class="container">
        <strong>회원가입 페이지</strong>
        <form @submit.prevent="submitForm">
            <div>
                <label for="email">ID</label>
                <input type="text" id="email" v-model="email"/>
            </div>
            <div>
                <label for="password">비밀번호</label>
                <input type="password" id="pw" v-model="pw"/>
            </div>
            <div>
                <label for="nickname">이름</label>
                <input type="text" id="nickname" v-model="nickname"/>
            </div>      
            <button type="submit">회원가입</button>
        </form>
    </div>   
</template>

<script>
import {registerUser} from '@/api/index';
    export default {
        data() {
            return {
                email: '',
                pw: '',
                nickname: '',
            };
        },
        methods: {
            async submitForm() {
                const userData = {
                    email: this.email,     
                    pw: this.pw,
                    nickname: this.nickname,
                };
                const { data } = await registerUser(userData);
                console.log(data);
                
                if(data.data.email != "" && data.data.pw != "" && data.data.nickname != ""){
                    alert('회원가입 성공');
                    this.$router.push('/');
                }else{
                    alert('회원가입 실패');
                }

                //this.initForm();
            },
            /*initForm(){
                this.email='';
                this.pw='';
                this.nickname='';
            },*/
            
        },
    }
</script>

<style scoped>
</style>