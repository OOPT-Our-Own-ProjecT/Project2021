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
        <div>
            <p>{{beforeSort}}</p>
        </div>
        
        <p>정렬후</p>
        <div v-for="(item, index) in arr2" v-bind:key=item.idx>
            <h1>{{ index }} - {{ item }}</h1>            
        </div>
        <p>{{arr2}}</p>
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
            beforeSort: [1, 10, 5, 8, 7, 6, 4, 3, 2, 9],
            arr: [1, 10, 5, 8, 7, 6, 4, 3, 2, 9],
            arr2: [],
            arr3: []
        }
    },
    created(){

    },
    methods: {
        selSort(){
            this.arr;
            this.arr2;
            var i, j, min, temp, index
            for(i=0; i<10; i++){
                min = 9999;
                for(j=i; j<10; j++){
                    if(min > this.arr[j]){
                        min = this.arr[j];
                        index = j;
                    }
                }
                temp = this.arr[i];
                this.arr[i] = this.arr[index];
                this.arr[index] = temp;
                this.arr2 = this.arr
                //this.arr3.push(this.arr2)
                //this.$set(this.arr2)
                this.arr2.push()
                console.log(this.arr2)
            }
                  
        }
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