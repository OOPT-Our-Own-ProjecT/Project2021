<template>
    <div>
        <div>
            <MainNB></MainNB>
            <br>
            <SortNB></SortNB>
        </div>
        <h2>mergesort</h2>
        <div>
            <textarea v-model="data"></textarea>
            <button @click="push(data)">push</button>
            <button @click="mergebutton()">merge</button>
            <button @click="erase()">erase</button>
        </div>
        <div>
            <div class="list">
                <div class="listdata" v-for="(item,idx) in origin_list"  v-bind:key=idx>
                    <div><h2>{{item}}</h2></div>
                </div>
            </div>
            <br>
            <div class="list2">
                <div class="listdata" v-for="(item,idx) in merge_list"  v-bind:key=idx>
                    <div><h2>{{item}}</h2></div>
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
            merge_list:[],
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
        mergebutton(){
            this.merge_list = []
            this.merge_list = this.mergeSort(this.origin_list)
        },
        mergeSort(array){
            if (array.length == 1){
                return array
            }
            const middleIndex = Math.floor(array.length / 2);
            const left = array.slice(0, middleIndex);
            const right = array.slice(middleIndex);
            const tmp_data =  this.merge(this.mergeSort(left), this.mergeSort(right));
            this.merge_list.push(tmp_data)
            return tmp_data
        },
        merge(left, right){
            const result = [];
            while(left.length!=0 && right.length!=0){
                left[0] <= right[0] ? result.push(left.shift()) : result.push(right.shift());
            }
            return [...result, ...left, ...right];
        },
        erase(){
            this.data = ""
            this.origin_list = []
            this.merge_list = []
        },
    }
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
    .list2{
        margin: auto;
        height: 100px;
        width: 90%;
        border: 1px solid;
        padding: 15px;
    }
    .listdata{
        width: 14%;
        float: left;
    }
    .group{
        border: 1px solid;
        width: 10%;
        float: left;
        margin: 10px;
    }
</style>