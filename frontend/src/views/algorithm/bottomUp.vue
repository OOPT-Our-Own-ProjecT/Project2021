<template>
    <div>
        <div>
            <MainNB></MainNB>
            <br>
            <AlgoNB></AlgoNB>
        </div>
        <h2>BOTTOMUP</h2>
        <h3>KnapSack Algorithm</h3>
        <div>
            무게 <textarea v-model="weight"></textarea>
            가격 <textarea v-model="price"></textarea>
            <button @click="push(weight,price)">push</button>
            <button @click="erase()">erase</button>
            <div class="list">
                <div>
                    가방 용량<textarea v-model="bag"></textarea>
                    <button @click="dp(bag)">값 구하기</button>
                </div>
                <div class="listdata">
                    <div><h4>무게</h4></div>
                    <div><h4>값</h4></div>
                </div>
                <div class="listdata" v-for="(item,idx) in origin_list"  v-bind:key=idx>
                    <div><h4>{{item.weight}}</h4></div>
                    <div><h4>{{item.price}}</h4></div>
                </div>
            </div>
            <br>
            <div v-show="max_value != -1">
                <h3>가장 많이 넣은 값 : {{max_value}}</h3>
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
            weight: "",
            price: "",
            bag: "",
            origin_list : [],
            max_value: -1
        }
    },
    created(){

    },
    methods: {
        push(weight,price){
            if(this.origin_list.length>=6) alert("OverFlow!!")
            else {
                if(isNaN(weight) || weight == "" || isNaN(price) || price == "") alert("숫자만 가능합니다.")
                else {
                    const tmp_list = {"weight" : weight, "price" : price, "value" : parseFloat(price/weight).toFixed(2)}
                    this.origin_list.push(tmp_list)
                }
            }
            this.weight = ""
            this.price = ""
            this.max_value = -1
        },
        erase(){
            this.origin_list = []
            this.weight = ""
            this.price = ""
            this.bag = ""
            this.max_value = -1
        },
        dp(bag){
            if(isNaN(bag) || bag == "") {
                alert("가방용량을 입력하세요.")
                return
            }
            this.bag = bag
            const list = []
            for(var a=0; a<=this.origin_list.length; a++){
                const col = []
                for(var b=0; b<=this.bag; b++){
                    col.push(0)
                }
                list.push(col)
            }
            for(var i=0; i<=this.origin_list.length; i++){
                for(var w=0; w<=this.bag; w++){
                    if(i==0 || w==0) list[i][w] = parseInt(0)
                    else if(this.origin_list[i-1].weight <=w){
                        list[i][w] = Math.max(parseInt(this.origin_list[i-1].price) + parseInt(list[i-1][w-this.origin_list[i-1].weight]), parseInt(list[i-1][w]))
                    }
                    else list[i][w] = list[i-1][w]
                }
            }
            this.max_value = list[this.origin_list.length][bag]
        },
    },
}
</script>

<style>
    .list{
        margin: auto;
        height: 200px;
        width: 75%;
        border: 1px solid;
    }
    .listdata{
        width: 14%;
        float: left;
    }
</style>