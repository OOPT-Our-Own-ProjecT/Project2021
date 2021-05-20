<template>
    <div>
        <strong>로그인 확인 페이지</strong>
        <h2>환영합니다. {{userData.nickname}} 님!</h2>
        
    </div>
</template>

<script>


export default{
    data: () => ({
            userData : {
                id : "",
                pw :  "",
            },
            //userList: [],
        }),
        
        

        methods: {
            

        },
}
</script>

<style>

</style>