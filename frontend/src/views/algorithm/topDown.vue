<template>
    <div>
        <div>
            <MainNB></MainNB>
            <br>
            <AlgoNB></AlgoNB>
        </div>
        <h2>TOPDOWN</h2>
        <div>
            <h3>A 행렬의 m제곱 구하기</h3>
            <br><br>
            <textarea v-model="arr_size"></textarea>
            <button @click="fix_size(arr_size)">N*N행렬 크기</button>
            <textarea v-model="arr_item"></textarea>
            <button @click="make_arr(arr_item)">행렬 입력</button>
            <textarea v-model="data"></textarea>
            <button @click="input(data)">m값 입력</button>
            <button @click="divide()">분할</button>
            <button @click="calc()">계산</button>
        </div>
        <div>
            <div class="list">
                <div class="listdata" v-for="(item,idx) in arr"  v-bind:key=idx>
                    <div><h2>{{item}}</h2></div>
                </div>
            </div>
        </div>
        <div>
            <div class="list" v-for="(item,idx) in divide_list"  v-bind:key=idx>
                분할 결과<br>
                <div class="listdata" v-for="(item2,idx) in item"  v-bind:key=idx>
                    <div><h2>{{item2}}</h2></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import MainNB from '@/components/mainNB.vue'
import AlgoNB from '@/components/algoNB.vue'

export default {
    components:{
        MainNB,
        AlgoNB,
    },

    computed: {

    },


	data () {
		return {
            arr_size:"",
            arr_item:"",
            data: "",
            list:[],
            arr:[],
            divide_list:[],
            calc_list:[],
        }
    },
    created(){

    },
    methods: {

        fix_size(arr_size){

            this.arr_size = arr_size

            alert(this.arr_size * this.arr_size + "개의 숫자를 입력해주세요")
        },
        make_arr(arr_item){

            this.arr_item = arr_item

            if(this.list.length < this.arr_size * this.arr_size){

                this.list.push(this.arr_item)
                console.log(this.list)
            }
            else{

                alert("꽉 참!!!")

            }

            if(this.list.length == this.arr_size * this.arr_size){

                var temp = []

                for(var i = 0; i < this.list.length; i++){

                    if(temp.length == this.arr_size){
                        
                        this.arr.push(temp)
                        temp = []
                    }
                    
                    temp.push(this.list[i])

                }

                this.arr.push(temp)


                console.log(this.arr)
            }

        },
        input(data){

            this.data = data
            this.divide_list = [[data]]
        },
        divide(){

            var temp_list = []

            if(this.divide_list[this.divide_list.length - 1].length == 1 && this.divide_list[this.divide_list.length - 1][0] == 1){
            
                alert("더 이상 나눌 수 없습니다!")
                return;
            }

            for(var i = 0; i < this.divide_list[this.divide_list.length - 1].length; i++){

                if(this.divide_list[this.divide_list.length - 1][i] == 1){

                    temp_list.push(1)
                    continue
                }

                if(this.divide_list[this.divide_list.length - 1][i] % 2 == 0){

                    if(!temp_list.includes(this.divide_list[this.divide_list.length - 1][i] / 2)){

                        temp_list.push(this.divide_list[this.divide_list.length - 1][i] / 2)
                    }
                    
                }
                else{



                    if(!temp_list.includes(this.divide_list[this.divide_list.length - 1][i] / 2 - 0.5)){

                        temp_list.push(this.divide_list[this.divide_list.length - 1][i] / 2 - 0.5)
                    }

                    if(!temp_list.includes(this.divide_list[this.divide_list.length - 1][i] / 2 - 0.5 + 1)){

                        temp_list.push(this.divide_list[this.divide_list.length - 1][i] / 2 - 0.5 + 1)
                    }

                }

            }

            this.divide_list.push(temp_list)

        },
        calc(){

            this.calc_list = []

            for(var i = this.divide_list.length - 1; i >= 0; i--){

                console.log(this.divide_list[i])

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
        float:left;
    }
</style>