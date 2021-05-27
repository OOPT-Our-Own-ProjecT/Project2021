<template>
    <div>
        <div>
            <MainNB></MainNB>
            <br>
            <SortNB></SortNB>
        </div>
        <h2>insertionsort</h2>
        <div>
            <button @click="inSort()">Sorting</button>
        </div>
        <br><br>
         <transition-group tag="ul" class="list">
            <li v-for="(item, index) in iSort._arr"
            v-bind:key="item"
            class="item"
            v-on:click="doRemove(index)">{{ item }}</li>
        </transition-group>
    </div>
</template>

<script>

class insertionSort{
    constructor(size){
        this._arr = [5, 54, 32, 48, 24, 3, 8];
        this.maxArrSize = size;
    }

    /*
    isEmpty(){
      return this._arr.length == 0;
    }

    isFull(){
        return this.maxArrSize == this._arr.length;
    }

    input(item){
        if(this.isFull()){
            alert("입력 가능 개수가 최대입니다.")
        }
        else{
            this._arr.push(item);
        }
    }
    */
    inSort(){

        /*
        if(this.isEmpty()){
            alert("입력이 하나도 없습니다.")
        }
        else{

            for(let i = 1; i < this._arr.length; i++){

                let cur = this._arr[i];
                let left = i - 1;

                while(left >= 0 && this._arr[left] > cur){
                    this._arr[left + 1] = this._arr[left];
                    left--;
                }

                this._arr[left + 1] = cur;

                let mes = "" + i + "회전 : "

                for(let j = 0; j < this._arr.length; j++){

                    mes += this._arr[j] + " "

                }

                console.log(mes);
            }

        }
        */
       for(let i = 1; i < this._arr.length; i++){

            let cur = this._arr[i];
            let left = i - 1;

            while(left >= 0 && this._arr[left] > cur){
                this._arr[left + 1] = this._arr[left];
                left--;
            }

            this._arr[left + 1] = cur;

        }
    }

}

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
            item: "",
            iSort : new insertionSort(7),
        }
    },
    created(){

    },
    methods: {
        /*
        input(data){
            this.iSort.input(data)
            this.item = ""
        },
        */
        inSort(){
            this.iSort.inSort()
        },
        doRemove: function (index) {
            this.list.splice(index, 1)
        },
    },
}
</script>

<style>
.list {
  width: 240px;
  padding: 0;
}
.item {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  margin: 4px;
  width: 40px;
  height: 40px;
  background: #f5f5f5;
}
/* 트랜지션 전용 스타일 */
.v-enter-active, .v-leave-active, .v-move {
  transition: all 1s;
}
.v-leave-active {
  position: absolute;
}
.v-enter, .v-leave-to {
  opacity: 0;
  background: #f9a3b1;
  transform: translateY(-30px);
}
</style>