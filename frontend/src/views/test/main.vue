<template>
    <div>
        <strong>메인페이지</strong>
        <br><br>
        <div>
            {{GET_MESSAGE}}
        </div>
        <br><br>
        <div>
          <input placeholder="ID 입력" v-model="userData.email">
          <input type="password" placeholder="비번 입력" v-model="userData.pw">
        </div>
        <br>
        <div>
            <button @click="getUser()">로그인</button>
            <button @click="$router.push('/signUp')">회원가입</button>
        </div>
        <br>
        <div v-show="userList != null">
            <div>
                <table id="userList">
                    <thead>
                        <tr>
                            <th>이메일</th>
                            <th>닉네임</th>
                            <th>기능</th>
                        </tr>
                    </thead>
                    <tbody id="userInfo">
                        <tr v-for="item in userList" v-bind:key=item.email>
                            <td>{{item.email}}</td>
                            <td>{{item.nickname}}</td>
                            <td><button @click="deleteUser(item)">삭제</button></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import {getUserAll , deleteUser, getUser} from '@/api/index';

import { mapGetters } from 'vuex'

const accountStore = 'accountStore'

    export default {
        data: () => ({
            userData : {
                email : "",
                pw :  "",
            },
            userList: [],
        }),

        computed:{
            ...mapGetters(accountStore, [
                'GET_MESSAGE'
            ]),
        },

        created() {
            this.getUserAll()
        },

        methods: {
            async getUserAll() {
                const{ data } = await getUserAll();
                this.userList = data.data;
            },


            async getUser(){
                const userData = {
                    email: this.userData.email,
                    pw: this.userData.pw,
                };
                const{ data } = await getUser(userData);
                if(data.data == ""){
                    alert(data.message)
                }
                else {
                    this.$session.set("user_email" , data.data.email)
                    this.$session.set("user_nickname" , data.data.nickname)
                    this.$router.push('loginSuccess')
                }
            },

            async deleteUser(user){
                const userData = {
                    email: user.email,
                    pw: user.pw,
                    nickname: user.nickname,
                };
                const { data } = await deleteUser(userData);
                alert(data.message)
                this.getUserAll()
            },

        },
    }
</script>

<style scoped>
    table{
        width: 40%;
        margin-left: auto;
        margin-right: auto;
        text-align: center;
    }
    table,tr,td{
        border : 1px solid black;
    }
</style>