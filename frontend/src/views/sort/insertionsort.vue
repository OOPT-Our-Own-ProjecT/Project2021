<template>
    <div>
        <div>
            <MainNB></MainNB>
            <br>
            <SortNB></SortNB>
        </div>
        <h2>insertionsort</h2>
        <div>
            <textarea v-model="data"></textarea>
            <button @click="push(data)">push</button>
            <button @click="insertionSort()">sort</button>
            <button @click="erase()">erase</button>
        </div>
        <div>
            <div class="list">
                <div class="listdata" v-for="(item,idx) in origin_list"  v-bind:key=idx>
                    <div><h2>{{item}}</h2></div>
                </div>
            </div>
        </div>
        <div>
            <div class="list" v-for="(item,idx) in insert_list"  v-bind:key=idx>
                {{idx+1}} 회전 결과<br>
                <div class="listdata" v-for="(item2,idx) in item"  v-bind:key=idx>
                    <div><h2>{{item2}}</h2></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import MainNB from '@/components/mainNB.vue'
import SortNB from '@/components/sortNB.vue'

export default {
    components:{
        MainNB,
        SortNB,
    },

    computed: {

    },

   data () {
      return {
            data: "" ,
            origin_list:[],
            insert_list:[],
        }
    },
    created(){

    },
    methods: {
        push(data){
            if(isNaN(data) || data == "") alert("숫자만 가능합니다.")
            else if(this.origin_list.length >=7) alert("OverFlow!!")
            else this.origin_list.push(parseFloat(data))
            this.data = ""
        },
        insertionSort(){
            this.insert_list = []
            const now = []

            for(var a=0; a<this.origin_list.length; a++){
                now.push(this.origin_list[a])
            }
            for(var i = 1; i < now.length; i++){

                const prev = []

                for(var b=0; b<now.length; b++){
                    prev.push(now[b])
                }

                var cur = now[i];
                console.log(typeof(now[i]))
                var left = i - 1;

                while(left >= 0 && now[left] > cur){
                    now[left + 1] = now[left];
                    left--;
                }

                now[left + 1] = cur;

                const tmp = []
                for(var k=0; k<now.length; k++){
                    tmp.push(now[k])
                }
                this.insert_list.push(tmp)
            }
        },
        erase(){
            this.data = ""
            this.origin_list = []
            this.now_list = []
            this.insert_list= []
        },
    },
}
</script>

<style>
    .list{
        margin: auto;
        height: 100px;
        width: 75%;
        border: 1px solid;
        padding: 15px;
    }
    .listdata{
        width: 14%;
        float: left;
    }
</style>