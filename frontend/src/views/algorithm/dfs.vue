<template>
    <div>
        <div>
            <MainNB></MainNB>
            <br>
            <AlgoNB></AlgoNB>
        </div>
        <h2>DFS</h2>
        <div>
            <button @click="start()">dfs</button>
            <button @click="start2()">bfs</button>
            <button @click="initialize()">initialize</button>
            <br><br>
            <div class="row" v-for="(item,idx1) in item"  v-bind:key=idx1>
                <div v-for="(item,idx2) in item" v-bind:key=idx2>
                    <div class = "col1" v-show="visited[idx1][idx2] == 0">
                        {{item}}
                    </div>
                    <div class = "col2" v-show="visited[idx1][idx2] == 1">
                        {{item}}
                    </div>
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
            item: [[0,9,10,19,20],
                [1,8,11,18,21],
                [2,7,12,17,22],
                [3,6,13,16,23],
                [4,5,14,15,24]],
            visited: [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
            time: 0,
            direction: [[-1,0],[1,0],[0,-1],[0,1]],
        }
    },
    created(){

    },
    methods: {
        start(){
            this.$set(this.visited[0], 0, 1)
            this.dfs(0,0)
        },
        start2(){
            this.$set(this.visited[0], 0, 1)
            this.bfs(0,0)
        },
        dfs(row,col){
            setTimeout(() => {
                var nx = -1;
                var ny = -1;
                for(var k=0; k<4; k++){
                    const dx = row+this.direction[k][0]
                    const dy = col+this.direction[k][1]
                    if(dx>=0 && dx<5 && dy>=0 && dy<5 && this.visited[dx][dy] == 0){
                        nx = dx
                        ny = dy
                        break;
                    }
                }//end for.
                if(nx!=-1 && ny!=-1){
                    this.$set(this.visited[nx], ny, 1)
                    this.dfs(nx,ny)
                }
            }, 100)
        },
        initialize(){
            this.visited = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        },
        bfs(row,col){
            setTimeout(() => {
                for(var k=0; k<4; k++){
                    const dx = row+this.direction[k][0]
                    const dy = col+this.direction[k][1]
                    if(dx>=0 && dx<5 && dy>=0 && dy<5 && this.visited[dx][dy] == 0){
                        this.$set(this.visited[dx], dy, 1)
                        this.bfs(dx,dy)
                    }
                }//end for.
            }, 100)
        }
    },
}

</script>

<style>
    .row{
        margin: auto;
        content: center;
        text-align: center;
        height: 100px;
        width: 500px;
        border: 1px solid black;
    }
    .col1{
        border:1px solid black;
        background-color:white;
        width:100px; height:100px;
        border-radius:75px;
        line-height:100px;
        width: 19.6%;
        height: 100%;
        text-align: center;
        float: left;
    }
    .col2{
        border:1px solid black;
        background-color:aqua;
        width:100px; height:100px;
        border-radius:75px;
        line-height:100px;
        width: 19.6%;
        height: 100%;
        text-align: center;
        float: left;
    }
</style>