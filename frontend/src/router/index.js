import Vue from 'vue'
import Router from 'vue-router'
//import Router
import Main from '@/views/test/main.vue'
import SignUp from '@/views/account/signUp.vue'
import LoginSuccess from '@/views/test/loginSuccess.vue'
import Stack from '@/views/ds/stack.vue'
import Queue from '@/views/ds/queue.vue'
//import Component

Vue.use(Router)

const routes = [
    {
        path: '/',
        name: 'Main',
        component: Main
    },
    {
        path: '/signUp',
        name: 'SignUp',
        component: SignUp
        //코드 스플리팅 적용
        //component: () => import('@/views/account/signUp.vue'),
    },
    {
        path: '/loginSuccess',
        name: 'loginSuccess',
        component: LoginSuccess
    },
    {
        path: '/stack',
        name: 'stack',
        component: Stack
    },
    {
        path: '/queue',
        name: 'queue',
        component: Queue
    },

]
//path 와 component 엮어주는 부분.

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
  })
//main.js에서 사용할 router를 정의하는 부분.


export default router