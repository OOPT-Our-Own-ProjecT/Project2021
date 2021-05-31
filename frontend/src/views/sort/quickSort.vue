<template>
    <div>
        <div>
            <MainNB></MainNB>
            <br>
            <SortNB></SortNB>
        </div>
        <h2>quicksort</h2>
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
                <button v-show="can_end == false" @click="divide()">divide</button>
                <h2 v-show="can_end == true"> QuickSort Finish!! </h2>
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
            this.divide_list = []
            this.can_end = false
            const tmp_list = []
            for(var i=0; i<this.origin_list.length; i++){
                tmp_list.push(this.origin_list[i])
            }
            if(tmp_list.length==0) alert("데이터를 넣어주세요")
            else this.divide_list.push(tmp_list)
        },
        divide(){
            const tmp_list = []
            for(var i=0; i<this.divide_list.length; i++){
                const list = this.divide_list[i]
                if(list.length == 1) tmp_list.push(list)
                else if(list.length==2){
                    const left = [];
                    const right = [];
                    if(list[0] < list[1]){
                        left.push(list[0])
                        right.push(list[1])
                    }
                    else{
                        left.push(list[1])
                        right.push(list[0])
                    }
                    tmp_list.push(left)
                    tmp_list.push(right)
                }
                else{
                    const pivot = list[0]
                    const pivot_list = []
                    const left = [];
                    const right = [];
                    for (var j = 0; j<list.length; j++) {
                        if (list[j] < pivot) left.push(list[j])
                        else if(list[j] > pivot) right.push(list[j]);
                        else pivot_list.push(list[j])
                    }
                    console.log(left)
                    console.log(pivot_list)
                    console.log(right)
                    if(left.length>0)tmp_list.push(left)
                    tmp_list.push(pivot_list)
                    if(right.length>0)tmp_list.push(right)
                }
            }
            this.divide_list = tmp_list
            if(this.divide_list.length == this.origin_list.length) this.can_end = true
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
        height: 400px;
        width: 90%;
        border: 1px solid;
        padding: 15px;
    }
    .group{
        border: 1px solid;
        width: 10%;
        float: left;
        margin: 10px;
    }
</style>