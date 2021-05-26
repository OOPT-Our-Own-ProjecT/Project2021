<template>
    <div>
        <div>
            <MainNB></MainNB>
            <br>
            <DSNB></DSNB>
        </div>
        <h2>Queue 실험실</h2>
        <div>
            <textarea v-model="item"></textarea>
            <button @click="enqueue(item)">Enqueue</button>
            <button @click="dequeue()">Dequeue</button>
        </div>
        <br><br>
        <div class="queue">
            <div v-for="item in queue._arr" v-bind:key=item.idx>
                <div class="queue_data">
                    {{item}}
                </div>
            </div>
        </div>
    </div>
</template>

<script>

class Queue {
  constructor(size) {
    this.maxQueueSize = size;
    this._arr = [];
    this.front = 0;
    this.rear = 0;
  }
  isEmpty(){
      return this.front == this.rear;
  }
  isFull(){
      return (this.rear + 1) % this.maxQueueSize == this.front;
  }
  enqueue(item) {
      if(this.isFull()){
          alert("큐가 포화상태입니다.")
      }
      else{
          this.rear = (this.rear + 1) % this.maxQueueSize;
          this._arr.push(item);
      }
  }
  dequeue() {
      if(this.isEmpty()){
          alert("큐가 비었습니다.")
      }
      else{
          this.front = (this.front + 1) % this.maxQueueSize;
          return this._arr.shift();
      }
  }
}

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
            queue : new Queue(6),
        }
    },
    created(){

    },
    methods: {
        enqueue(data){
            this.queue.enqueue(data)
            this.item = ""
        },
        dequeue(){
            this.queue.dequeue()
        },
    },
}
</script>

<style>
    .queue{
        margin: auto;
        height: 100px;
        width: 500px;
        border: 1px solid;
        text-align: center;
        align-content: center;
        transform: rotate(180deg);
    }
    .queue_data{
        background-color: rgba(226, 83, 226, 0.795);
        margin: auto;
        float: right;
        height: 100px;
        width: 98px;
        border: 1px solid;
        transform: rotate(180deg);
    }
</style>