<template>
    <div class="container">
        <strong>회원가입 페이지</strong>
        <form @submit.prevent="submitForm">
            <div>
                <label for="id">ID</label>
                <input type="text" id="id" v-model="id"/>
            </div>
            <div>
                <label for="name">이름</label>
                <input type="text" id="name" v-model="name"/>
            </div>
            <div>
                <label for="password">비밀번호</label>
                <input type="password" id="password" v-model="password"/>
            </div>
            <div>
                <label for="passwordConfirm">비밀번호 확인</label>
                <input type="password" id="passwordConfirm" v-model="passwordConfirm"/>
            </div>
            <button type="submit">회원가입</button>
            <p>{{ logMessage }}</p>
        </form>
    </div>
    
</template>

<script>
import {registerUser} from '@/api/index';
    export default {
        //name: 'SignupForm',
        data() {
            return {
                id: '',
                name: '',
                password: '',
                passwordConfirm: '',
                logMessage: '',

            };
        },
        methods: {
            async submitForm() {
                const userData = {
                    id: this.id,
                    name: this.name,
                    password: this.password,
                    passwordConfirm: this.passwordConfirm,
                };
                const { data } = await registerUser(userData);
                console.log(data.id);
                console.log(data.name);
                //this.logMessage = '${data.id} 님이 가입되었습니다.';

                this.initForm();
            },
            initForm(){
                this.id='';
                this.name='';
                this.password='';
                this.passwordConfirm='';
            },
            
        },
    }
</script>

<style scoped>
</style>