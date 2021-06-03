<template>
    <div>
        <div>
            <MainNB></MainNB>
            <br>
            <AlgoNB></AlgoNB>
        </div>
        <h2>BINARYSEARCH</h2>
        <textarea v-model="data"></textarea>
        <button @click="push(data)">push</button>
        <button @click="insertionSort()">sort</button>
        <button @click="erase()">erase</button>
        <div>
            <div class="list">
                <div class="listdata" v-for="(item,idx) in origin_list"  v-bind:key=idx>
                    <!-- <div class="round" @click="binarySearch(item)"><h2>{{item}}</h2></div> -->
                    <div class="round" v-show="check_list[idx] == 0" @click="binarySearch(item)"><h2>{{item}}</h2></div>
                    <div class="round2" v-show="check_list[idx] == 1" @click="binarySearch(item)"><h2>{{item}}</h2></div>
                    <div class="round3" v-show="check_list[idx] == 2" @click="binarySearch(item)"><h2>{{item}}</h2></div>
                    <div class="round4" v-show="check_list[idx] == 3" @click="binarySearch(item)"><h2>{{item}}</h2></div>
                    <div class="round5" v-show="check_list[idx] == 4" @click="binarySearch(item)"><h2>{{item}}</h2></div>
                </div>
            </div>
        </div>
        <div>
            <h3 v-show="find_num!=''"> 찾는 숫자 : {{find_num}}</h3>
            <br><br>
            <div class="list" v-for="(item,idx) in binary_list"  v-bind:key=idx>
                <div class="round6">{{item.mid}}</div>
                <div><h3>{{item.message}}</h3></div>
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
            data: "",
            origin_list:[],
            check_list:[],
            insert_list:[],
            find_num : "",
            left:"",
            right:"",
            flag: false,
            binary_list:[],
        }
    },
    created(){

    },
    methods: {
        push(data){
            if(isNaN(data) || data == "") alert("숫자만 가능합니다.")
            else if(this.origin_list.length >=10) alert("OverFlow!!")
            else {
                this.origin_list.push(parseFloat(data))
                this.check_list.push(0)
            }
            this.data = ""
            this.flag = false
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
            this.origin_list = this.insert_list[this.insert_list.length-1]
            this.flag = true
        },
        erase(){
            this.data = ""
            this.origin_list = []
            this.insert_list= []
            this.binary_list = []
            this.check_list = []
            this.find_num = ""
        },
        binarySearch(item){
            if(!this.flag){
                alert("배열 정렬버튼을 눌러주세요.")
                return
            }
            const tmp = []
            for(var i=0; i<this.check_list.length; i++){
                tmp.push(0)
            }
            this.check_list = tmp
            this.find_num = item
            this.binary_list = []
            this.left = 0
            this.right = this.origin_list.length-1
            var mid = Math.floor((this.left+this.right)/2)
            var time = 1
            while(this.right - this.left >=0){
                const mid_num = this.origin_list[mid]
                this.$set(this.check_list, mid, time)
                if(mid_num < item) {
                    this.binary_list.push({"mid" : mid_num , "message" : "숫자가 더 큽니다."})
                    this.left = mid+1
                }
                else if(mid_num > item) {
                    this.binary_list.push({"mid" : mid_num , "message" : "숫자가 더 작습니다."})
                    this.right = mid-1
                }
                else {
                    this.binary_list.push({"mid" : mid_num , "message" : "찾았습니다."})
                    break
                }
                time++
                mid = Math.floor((this.left+this.right)/2)
            }
        }
    },
}
</script>

<style>
    .list{
        margin: auto;
        height: 90px;
        width: 75%;
        border: 1px solid;
        padding: 15px;
    }
    .listdata{
        margin-top: 25px;
        width: 10%;
        float: left;
    }
    .round{
        border:1px solid black;
        background-color:white;
        width:45px; height:45px;
        border-radius:75px;
        line-height:15px;
        text-align: center;
        float: left;
    }
    .round2{
        border:1px solid black;
        background-color:red;
        width:45px; height:45px;
        border-radius:75px;
        line-height:15px;
        text-align: center;
        float: left;
    }
    .round3{
        border:1px solid black;
        background-color:orange;
        width:45px; height:45px;
        border-radius:75px;
        line-height:15px;
        text-align: center;
        float: left;
    }
    .round4{
        border:1px solid black;
        background-color:yellow;
        width:45px; height:45px;
        border-radius:75px;
        line-height:15px;
        text-align: center;
        float: left;
    }
    .round5{
        border:1px solid black;
        background-color:green;
        width:45px; height:45px;
        border-radius:75px;
        line-height:15px;
        text-align: center;
        float: left;
    }
    .round6{
        border:1px solid black;
        background-color:aqua;
        width:45px; height:45px;
        border-radius:75px;
        line-height:45px;
        text-align: center;
        float: left;
    }
</style>