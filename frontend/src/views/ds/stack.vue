<template>
    <div>
        <div>
            <NavigationBar></NavigationBar>
        </div>
        <h2>Stack 실험실</h2>
        <div>
            <textarea v-model="item"></textarea>
            <button @click="push(item)">Push</button>
            <button @click="pop()">Pop</button>
        </div>
        <div v-for="item in stack" v-bind:key=item.idx>
            <div>{{item}}</div>
        </div>
    </div>
</template>

<script>

class Stack {
  constructor() {
    this._arr = [];
  }
  push(item) {
    this._arr.push({
            idx : this._arr.length,
            data: item,
        });
  }
  pop() {
    return this._arr.pop();
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
            stack : new Stack(),
        }
    },
    created(){

    },
    methods: {
        push(data){
            this.stack.push(data)
            this.item = ""
        },
        pop(){
            this.stack.pop()
        },
    },
}
</script>

<style>

</style>