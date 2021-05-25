<template>
    <div>
        <div>
            <NavigationBar></NavigationBar>
        </div>
        <h2>Queue 실험실</h2>
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
  }
  enqueue(item) {
    this._arr.push(item);
  }
  dequeue() {
    return this._arr.shift();
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
            item: "",
            queue : new Queue(),
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

</style>