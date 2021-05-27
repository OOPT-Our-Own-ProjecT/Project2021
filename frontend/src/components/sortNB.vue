<template>
   <div class="navigation">
       <table id="nav">
            <tbody id="navInfo">
                <td v-for="item in items" v-bind:key=item.titla>
                    <button @click="move(item.path)" style="background-color: aqua;">{{item.title}}</button>
                </td>
            </tbody>
        </table>
   </div>
</template>

<script>
export default {
	data () {
		return {
            items: [
                { title: 'Insertion', path: '/insertionSort'},
                { title: 'Selection', path: '/selectionSort'},
                { title: 'Bubble', path: '/bubbleSort'},
                { title: 'Merge', path: '/mergeSort'},
                { title: 'Quick', path: '/quickSort'},
            ],
        }
    },
    methods: {
        move(path){
            this.$router.push(path)
        },
    },
}
</script>

<style>
    table{
        width: 40%;
        margin-left: auto;
        margin-right: auto;
        text-align: center;
    }
</style>
