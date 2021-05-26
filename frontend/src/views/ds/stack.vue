<template>
    <div>
        <div>
            <MainNB></MainNB>
            <br>
            <DSNB></DSNB>
        </div>
        <h2>Stack 실험실</h2>
        <div>
            <textarea v-model="item"></textarea>
            <button @click="push(item)">Push</button>
            <button @click="pop()">Pop</button>
        </div>
        <br><br>
        <div class="stack">
            <div v-for="item in stack._arr" v-bind:key=item.idx>
                <div class="stack_data">
                    <h1>{{item}}</h1>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

class Stack {
    constructor() {
        this._arr = [];
    }
    push(item) {
        if(this._arr.length != 5) {
            if(item == "") alert("빈 값은 넣을 수 없습니다.")
            else this._arr.push(item)
        }
        else alert("OverFlow!!")
    }
    pop() {
        if(this._arr.length != 0) this._arr.pop()
        else alert("UnderFlow!!")
    }
}//Class Stack.

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
    .stack{
        margin: auto;
        height: 500px;
        width: 50%;
        border: 1px solid;
        text-align: center;
        transform: rotate(180deg);
    }
    .stack_data{
        background-color: aqua;
        margin: auto;
        height: 100px;
        width: 100%;
        border: 1px solid;
        transform: rotate(180deg);
    }
</style>