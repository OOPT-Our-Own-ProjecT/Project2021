<template>
    <div>
        <div>
            <MainNB></MainNB>
            <br>
            <SortNB></SortNB>
        </div>
        <h2>selectionsort</h2>
        <button @click="selSort()">Sort</button>
        <p>정렬전</p>
        <div class="list">
        <div class="listdata" v-for="(item,idx) in beforeSort"  v-bind:key=idx>
                <div><h2>{{item}}</h2></div>
        </div>
        </div>
        <p>정렬후</p>
        <div class="list" v-for="(item,idx) in arr3"  v-bind:key=idx>
            {{idx+1}} 회전 결과<br>
            <div class="listdata" v-for="(item2,idx) in item"  v-bind:key=idx>
                <div><h2>{{item2}}</h2></div>
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
            beforeSort: [1, 10, 5, 8, 7, 6, 4],
            arr: [1, 10, 5, 8, 7, 6, 4],
            arr3: []
        }
    },
    created(){

    },
    methods: {
        selSort(){
            
            var i, j, min, temp, index
            for(i=0; i<this.arr.length; i++){
                min = 9999;
                for(j=i; j<this.arr.length; j++){
                    if(min > this.arr[j]){
                        min = this.arr[j];
                        index = j;
                    }
                }
                
                temp = this.arr[i];
                this.arr[i] = this.arr[index];
                this.arr[index] = temp;
                var arr2 = [];
                for(var k=0; k<this.arr.length; k++){
                    arr2[k] = this.arr[k]
                    //console.log(this.arr2)
                }
                console.log(arr2)
                
                //console.log(this.arr2)
                this.arr3.push(arr2)
            }
            
                  
        }
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