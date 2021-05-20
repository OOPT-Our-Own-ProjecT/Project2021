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
        <br>
        <div v-show="userList != null">
            <div>
                <table id="userList">
                    <thead>
                        <tr>
                            <th>이메일</th>
                            <th>닉네임</th>
                        </tr>
                    </thead>
                    <tbody id="userInfo">
                        <tr v-for="item in userList" v-bind:key=item.email>
                            <td>{{item.email}}</td>
                            <td>{{item.nickname}}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import {getUserAll} from '@/api/index';
    export default {
        data: () => ({
            userData : {
                id : "",
                pw :  "",
            },
            userList: [],
        }),

        created() {
            this.getUserAll()
        },

        methods: {
            async getUserAll() {
                const{ data } = await getUserAll();
                this.userList = data.data
            },

            login(){
                console.log("로그인 메소드 실행")
                console.log(this.userData.id)
                console.log(this.userData.pw)
            }
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