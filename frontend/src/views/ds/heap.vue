<template>
    <div>
        <div>
            <MainNB></MainNB>
            <br>
            <DSNB></DSNB>
        </div>
        <h2>Heap 실험실</h2>
        <div>
            <textarea v-model="item"></textarea>
            <button @click="insert(item)">insert</button>
            <button @click="pop()">Pop</button>
        </div>
        <br>
        <div>
            <h1>MAX HEAP</h1>
            <div>
                <h3>마지막 출력</h3>
                <div class="round" v-if="max_extract != 0">{{max_extract}}</div>
            </div>
            <br>
            <div class="heap">
                <div class="heapdata" v-for="(item,idx) in maxheap.heap"  v-bind:key=idx>
                    <div>{{idx}}</div><br>
                    <div><h1>{{item}}</h1></div>
                </div>
            </div>
        </div>
        <div>
            <h1>MIN HEAP</h1>
            <div>
                <h3>마지막 출력</h3>
                <div class="round" v-if="min_extract != 0">{{min_extract}}</div>
            </div>
            <br>
            <div class="heap">
                <div class="heapdata" v-for="(item,idx) in minheap.heap"  v-bind:key=idx>
                    <div>{{idx}}</div><br>
                    <div><h1>{{item}}</h1></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

class MaxHeap {
    constructor() {
        this.heap = [];
    }

    insert(value) {
        if(isNaN(value) || value == "") alert("숫자만 가능합니다.")
        else if(this.heap.length==7) alert("더이상 넣을 수 없습니다.")
        else {
            this.heap.push(value);
            this.bubbleUp();
        }
    }

    bubbleUp() {
        let cur_idx = this.heap.length - 1
        while (cur_idx > 0) {
            const parent_idx = Math.floor((cur_idx - 1) / 2)
            if (this.heap[parent_idx] >= this.heap[cur_idx]) break
            [this.heap[cur_idx], this.heap[parent_idx]] = [this.heap[parent_idx], this.heap[cur_idx]]
            cur_idx = parent_idx;
        }
    }//맥스힙 순서 맞추기.

    extractMax() {
        if(this.heap.length==0) alert("UnderFlow!!");
        else{
            const max = this.heap[0]
            if(this.heap.length!=1){
                this.heap[0] = this.heap.pop()
                this.sinkDown(0)
            }
            else this.heap.pop()
            return max;
        }
        return "";
    }

    sinkDown(idx) {
        const left_idx = 2 * idx + 1
        const right_idx = 2 * idx + 2
        const length = this.heap.length
        let largest_idx = idx
        if (left_idx < length && this.heap[left_idx] > this.heap[largest_idx]) largest_idx = left_idx
        if (right_idx < length && this.heap[right_idx] > this.heap[largest_idx]) largest_idx = right_idx
        if (largest_idx !== idx) {
            [this.heap[idx], this.heap[largest_idx]] = [this.heap[largest_idx],this.heap[idx]]
            this.sinkDown(largest_idx)
        }
    }//맥스힙 순서 맞추기.
}//Class MaxHeap.

class MinHeap {
    constructor() {
        this.heap = [];
    }

    insert(value) {
        if(isNaN(value) || value == "") alert("숫자만 가능합니다.")
        else if(this.heap.length==7) alert("더이상 넣을 수 없습니다.")
        else {
            this.heap.push(value);
            this.bubbleUp();
        }
    }

    bubbleUp() {
        let cur_idx = this.heap.length - 1
        while (cur_idx > 0) {
            const parent_idx = Math.floor((cur_idx - 1) / 2)
            if (this.heap[parent_idx] <= this.heap[cur_idx]) break
            [this.heap[cur_idx], this.heap[parent_idx]] = [this.heap[parent_idx], this.heap[cur_idx]]
            cur_idx = parent_idx;
        }
    }//맥스힙 순서 맞추기.

    extractMin() {
        if(this.heap.length==0) alert("UnderFlow!!");
        else{
            const min = this.heap[0]
            if(this.heap.length!=1){
                this.heap[0] = this.heap.pop()
                this.sinkDown(0)
            }
            else this.heap.pop()
            return min;
        }
        return "";
    }

    sinkDown(idx) {
        const left_idx = 2 * idx + 1
        const right_idx = 2 * idx + 2
        const length = this.heap.length
        let smallest_idx = idx
        if (left_idx < length && this.heap[left_idx] < this.heap[smallest_idx]) smallest_idx = left_idx
        if (right_idx < length && this.heap[right_idx] < this.heap[smallest_idx]) smallest_idx = right_idx
        if (smallest_idx !== idx) {
            [this.heap[idx], this.heap[smallest_idx]] = [this.heap[smallest_idx],this.heap[idx]]
            this.sinkDown(smallest_idx)
        }
    }//맥스힙 순서 맞추기.
}//Class MaxHeap.


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
            item: "",
            max_extract: "",
            min_extract: "",
            maxheap : new MaxHeap(),
            minheap : new MinHeap(),
        }
    },
    created(){

    },
    methods: {
        insert(data){
            this.maxheap.insert(data)
            this.minheap.insert(data)
            this.item = ''
        },
        pop(){
            this.max_extract = this.maxheap.extractMax()
            this.min_extract = this.minheap.extractMin()
        },
    },
}
</script>

<style>
    .round{
        background-color:aqua;
        border:1px solid black;
        width:45px; height:45px;
        border-radius:75px;
        text-align:center;
        margin: auto;
        padding: auto;
        font-size:15px; color:black; font-weight:bold;
        vertical-align:middle;
        line-height:45px;
    }
    .heap{
        margin: auto;
        height: 100px;
        width: 75%;
        border: 1px solid;
        padding: 15px;
    }
    .heapdata{
        width: 14%;
        float: left;
    }
</style>