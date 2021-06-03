<template>
    <div>
        <div>
            <MainNB></MainNB>
            <br>
            <AlgoNB></AlgoNB>
        </div>
        <h2>DFS/BFS(2)</h2>
        <button @click="bfs()">BFS</button>
        <button @click="dfs()">DFS</button>
        <button @click="initialize()">initialize</button>
        <br><br>
        <p>
            <img src = "https://www.fun-coding.org/00_Images/BFSDFS.png" alt>
        </p>
        <br><br>
        <br><br>
        <transition-group tag="ul" class="list">
            <li v-for ="(item, index) in filteredList"
                :data-index="index"
                :key="item"
                class="item"
            >{{ item }}
            </li>
        </transition-group>
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
	data () {
		return {
            current : 1,
            graph : {A: ["B", "C"],
                B: ["A", "D"],
                C: ["A", "G", "H", "I"],
                D: ["B", "E", "F"],
                E: ["D"],
                F: ["D"],
                G: ["C"],
                H: ["C"],
                I: ["C", "J"],
                J: ["I"]
            },
            visited : [],
            queue : [],
            stack : [],
            start : "A",
        }
    },
    created(){

    },
    
    computed: {
        filteredList() {
            return this.visited;
        }
    },

    methods: {

        bfs(){

            this.queue.push(this.start);

            while(this.queue.length != 0){

                const cur = this.queue.shift();

                if(!this.visited.includes(cur)){
                    
                    this.visited.push(cur);
                    this.queue = [...this.queue, ...this.graph[cur]];

                }

            }

            console.log(this.visited);

        },
        dfs(){

            this.stack.push(this.start);

            while(this.stack.length !== 0){

                const cur = this.stack.pop();

                if(!this.visited.includes(cur)){
                    
                    this.visited.push(cur);
                    this.stack = [...this.stack, ...this.graph[cur]];

                }

            }

        },
        initialize(){
            this.visited = []
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
    transition: opacity 1s, transform 1s;
    }
    .v-leave-active {
    position: absolute;
    }
    .v-enter {
    opacity: 0;
    transform: translateY(-20px);
    }
    .v-leave-to {
    opacity: 0;
    transform: translateY(20px);
    }
</style>