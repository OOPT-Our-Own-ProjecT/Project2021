<template>
    <div>
        <div>
            <NavigationBar></NavigationBar>
        </div>
        <h2>Queue 실험실</h2>
        <div>
            <textarea v-model="size"></textarea>
            <button @click="inputSize(size)">Queue Size</button>
        </div>
        <div>
            <textarea v-model="item"></textarea>
            <button @click="enqueue(item)">Enqueue</button>
            <button @click="dequeue()">Dequeue</button>
        </div>
        <div v-for="item in queue" v-bind:key=item.idx>
            <div>{{item}}</div>
        </div>
    </div>
</template>

<script>

class Queue {
  constructor() {
    this._arr = [];
    this.front = 0;
    this.rear = 0;
  }
  inputSize(size){
      this.size = size;
  }
  isEmpty(){
      return this.front == this.rear;
  }
  isFull(){
      return (this.rear + 1) % this.size == this.front;
  }
  enqueue(item) {
      if(this.isFull()){
          console.log(new Error("큐가 포화상태입니다."))
      }
      else{
          this.rear = (this.rear + 1) % this.size;
          this._arr.push(item);
      }
  }
  dequeue() {
      if(this.isEmpty()){
          console.log(new Error("큐가 비었습니다."));
      }
      else{
          this.front = (this.front + 1) % this.size;
          return this._arr.shift();
      }
  }
}

import NavigationBar from '@/components/navigationBar.vue'

export default {
    components:{
        NavigationBar
    },

    computed: {

    },


	data () {
		return {
            size: "",
            item: "",
            queue : new Queue(),
        }
    },
    created(){

    },
    methods: {
        inputSize(size){
            this.size = size
            console.log(size);
        },
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

</style>