<template>
   <div class="navigation">
       <table id="nav">
            <tbody id="navInfo">
                <td v-for="item in items" v-bind:key=item.titla>
                    <button @click="move(item.path)">{{item.title}}</button>
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
                { title: 'Stack', path: '/stack'},
                { title: 'Menu 2', path: '/loginSuccess'},
                { title: 'Menu 3', path: '/loginSuccess'},
                { title: 'Menu 4', path: '/loginSuccess'},
                { title: 'Menu 5', path: '/loginSuccess'},
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
