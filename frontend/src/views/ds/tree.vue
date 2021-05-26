<template>
    <div>
        <div>
            <MainNB></MainNB>
            <br>
            <DSNB></DSNB>
        </div>
        <h2>Tree 실험실</h2>
        <button @click="traverse(tree)">On</button>
    </div>
</template>

<script>
class Node {
    constructor(content, children = []) {
        this.content = content;
        this.children = children;
    }
}

import MainNB from '@/components/mainNB.vue'
import DSNB from '@/components/dsNB.vue'

export default {
    components:{
        MainNB,
        DSNB,
    },

    computed: {

    },


	data () {
		return {
            tree: new Node('hello',[
                new Node('world'),
                new Node('and'),
                new Node('fun',[
                new Node('javascript!')
                ])
            ])
        }
    },
    created(){

    },
    methods: {
        traverse(node){
        console.log(node.content);
        for(let child of node.children){
                this.traverse(child);
            }
        }
    },
}
</script>

<style>

</style>