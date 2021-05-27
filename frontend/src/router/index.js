import Vue from 'vue'
import Router from 'vue-router'
//import Router
import Main from '@/views/test/main.vue'
import SignUp from '@/views/account/signUp.vue'
import LoginSuccess from '@/views/test/loginSuccess.vue'
//main
import Stack from '@/views/ds/stack.vue'
import Queue from '@/views/ds/queue.vue'
import Tree from '@/views/ds/tree.vue'
import Heap from '@/views/ds/heap.vue'
import PriorityQueue from '@/views/ds/priorityQueue.vue'
//data structure
import InsertionSort from '@/views/sort/insertionSort.vue'
import SelectionSort from '@/views/sort/selectionSort.vue'
import BubbleSort from '@/views/sort/bubbleSort.vue'
import MergeSort from '@/views/sort/mergeSort.vue'
import QuickSort from '@/views/sort/quickSort.vue'
//sort
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
    {
        path: '/tree',
        name: 'tree',
        component: Tree
    },
    {
        path: '/heap',
        name: 'heap',
        component: Heap
    },
    {
        path: '/priorityQueue',
        name: 'priorityQueue',
        component: PriorityQueue
    },
    {
        path: '/insertionSort',
        name: 'insertionSort',
        component: InsertionSort
    },
    {
        path: '/selectionSort',
        name: 'selectionSort',
        component: SelectionSort
    },
    {
        path: '/bubbleSort',
        name: 'bubbleSort',
        component: BubbleSort
    },
    {
        path: '/mergeSort',
        name: 'mergeSort',
        component: MergeSort
    },
    {
        path: '/quickSort',
        name: 'quickSort',
        component: QuickSort
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