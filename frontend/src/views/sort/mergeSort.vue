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
            <button @click="start()">start</button>
            <button @click="erase()">erase</button>
        </div>
        <div>
            <div class="list">
                <div class="listdata" v-for="(item,idx) in origin_list"  v-bind:key=idx>
                    <div><h2>{{item}}</h2></div>
                </div>
            </div>
            <br>
            <div class="list2" v-show="divide_list.length > 0">
                <button v-show="can_merge == false && can_end == false" @click="divide()">divide</button>
                <button v-show="can_merge == true && can_end == false" @click="merge()">merge</button>
                <h2 v-show="can_end == true"> MergeSort Finish!! </h2>
                <div v-for="(item,idx) in divide_list"  v-bind:key=idx>
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
            divide_list:[],
            can_merge: false,
            can_end: false,
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
            this.divide_list = []
            this.can_end = false
        },
        start(){
            const tmp_list = []
            for(var i=0; i<this.origin_list.length; i++){
                tmp_list.push(this.origin_list[i])
            }
            this.divide_list.push(tmp_list)
        },
        divide(){
            const tmp_list = []
            for(var i=0; i<this.divide_list.length; i++){
                const divide_data = this.divide_list[i]
                if(divide_data.length ==1) tmp_list.push(divide_data)
                else{
                    const middleIndex = Math.floor(divide_data.length / 2);
                    const left = divide_data.slice(0,middleIndex)
                    const right = divide_data.slice(middleIndex, divide_data.length)
                    tmp_list.push(left)
                    tmp_list.push(right)
                }
            }//end for.
            this.divide_list = tmp_list
            const can_merge = this.all_divide()
            if(can_merge) this.can_merge = true
        },
        merge(){
            const tmp_list = []
            for(var i=0; i<this.divide_list.length; i+=2){
                if(i==this.divide_list.length-1) tmp_list.push(this.divide_list[i])
                else tmp_list.push(this.mergesort(this.divide_list[i] , this.divide_list[i+1]))
            }
            this.divide_list = tmp_list
            if(this.divide_list.length == 1){
                this.can_merge = false
                this.can_end = true
            }
        },
        all_divide(){
            for(var i=0; i<this.divide_list.length; i++){
                if(this.divide_list[i].length != 1) return false
            }
            return true
        },
        mergesort(left, right){
            const result = [];
            while(left.length!=0 && right.length!=0){
                left[0] <= right[0] ? result.push(left.shift()) : result.push(right.shift());
            }
            return [...result, ...left, ...right];
        },
        erase(){
            this.data = ""
            this.origin_list = []
            this.divide_list = []
            this.can_end = false
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
        height: 350px;
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