<template>
    <div>
        <div>
            <MainNB></MainNB>
            <br>
            <SortNB></SortNB>
        </div>
        <h2>mergesort</h2>
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

        }
    },
    created(){

    },
    methods: {

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