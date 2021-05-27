<template>
    <div>
        <div>
            <MainNB></MainNB>
            <br>
            <DSNB></DSNB>
        </div>
        <h2>Priority Queue 실험실</h2>
        <div>
            <textarea v-model="priority"></textarea>
            <textarea v-model="value"></textarea>
            <button @click="enqueue(priority,value)">enqueue</button>
            <button @click="dequeue()">dequeue</button>
        </div>
        <div>
            <div class="pq">
                <div class="pqdata">
                    <div><h3>우선순위</h3></div>
                    <div><h3>값</h3></div>
                </div>
                <div class="pqdata" v-for="(item,idx) in PQ.heap"  v-bind:key=idx>
                    <div><h2>{{item.key}}</h2></div>
                    <div><h2>{{item.value}}</h2></div>
                </div>
            </div>
        </div>
        <div>
            <h3>마지막 DEQUEUE</h3>
            <div class="round" v-if="dequeue_data != undefined && dequeue_data !=''">{{dequeue_data.key}} , {{dequeue_data.value}}</div>
        </div>
    </div>
</template>

<script>

class Heap {
    constructor() {
        this.heap = []
    }

    left_idx = (parentIndex) => parentIndex * 2 + 1
    right_idx = (parentIndex) => parentIndex * 2 + 2
    parent_idx = (childIndex) => Math.floor((childIndex - 1) / 2)

    peek = () => this.heap[0] // 항상 최상위 노드가 peek 가 된다.

    insert = (key, value) => {
        const node = { key, value }
        this.heap.push(node)
        this.heapifyUp()
    }

    heapifyUp = () => {
        let index = this.heap.length - 1 // 계속해서 변하는 index 값
        const lastInsertedNode = this.heap[index]

        // 루트노드가 되기 전까지
        while (index > 0) {
            const parentIndex = this.parent_idx(index)

            if (this.heap[parentIndex].key > lastInsertedNode.key) {
                this.heap[index] = this.heap[parentIndex]
                index = parentIndex
            }
            else break
        }
        this.heap[index] = lastInsertedNode
    }

    remove = () => {
        const count = this.heap.length
        const rootNode = this.heap[0]
        if (count <= 0) return undefined
        if (count === 1) this.heap = []
        else {
            this.heap[0] = this.heap.pop() // 끝에 있는 노드를 부모로 만들고
            this.heapifyDown() // 다시 min heap 의 형태를 갖추도록 한다.
        }
        return rootNode
    }
    heapifyDown = () => {
        let index = 0
        const count = this.heap.length
        const rootNode = this.heap[index]

        // 계속해서 left child 가 있을 때 까지 검사한다.
        while (this.left_idx(index) < count) {
            const leftChildIndex = this.left_idx(index)
            const rightChildIndex = this.right_idx(index)
            const smallerChildIndex = rightChildIndex < count && this.heap[rightChildIndex].key < this.heap[leftChildIndex].key ? rightChildIndex : leftChildIndex
            if (this.heap[smallerChildIndex].key <= rootNode.key) {
                this.heap[index] = this.heap[smallerChildIndex]
                index = smallerChildIndex
            }
            else break
        }
        this.heap[index] = rootNode
    }
}//Class Heap.

class PriorityQueue extends Heap {
  constructor() {
    super()
  }

  enqueue = (priority, value) => this.insert(priority, value)
  dequeue = () => this.remove()
  isEmpty = () => this.heap.length <= 0
}//Class ProrityQueue.


import MainNB from '@/components/mainNB.vue'
import DSNB from '@/components/dsNB.vue'

export default {
    components:{
        MainNB,
        DSNB,
    },

    computed: {

    },


	data () {
		return {
            PQ : new PriorityQueue(),
            dequeue_data: "",
            dequeue_list: [],
            priority: "",
            value: "",
        }
    },
    created(){

    },
    methods: {
        enqueue(priority, value){
            if(this.PQ.heap.length>=6) alert("OverFlow!!")
            else {
                if(isNaN(priority) || priority == "") alert("숫자만 가능합니다.")
                else if(value == "") alert("값을 넣어주세요.")
                else this.PQ.enqueue(priority,value)
            }
            this.priority = ""
            this.value = ""
        },
        dequeue(){
            const node = this.PQ.dequeue();
            this.dequeue_data = node
            if(node == undefined) alert("UnderFlow!!")
        },
    },
}
</script>

<style>
    .pq{
        margin: auto;
        height: 100px;
        width: 75%;
        border: 1px solid;
        padding: 15px;
    }
    .pqdata{
        width: 14%;
        float: left;
    }
    .round{
        background-color:aqua;
        border:1px solid black;
        width:100px; height:100px;
        border-radius:75px;
        text-align:center;
        margin: auto;
        padding: auto;
        font-size:15px; color:black; font-weight:bold;
        vertical-align:middle;
        line-height:100px;
    }
</style>