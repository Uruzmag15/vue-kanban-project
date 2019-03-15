<template>
    <div>
        <input type="text" name="" v-model="login" placeholder="Логин">
        <input type="password" name="" v-model="password" placeholder="Пароль">
        <button @click="setLogin">Вход</button>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                login: '',
                password: '',
            }
        },
        methods: {
            setLogin() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/create/",
                    type: "POST",
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        console.log(response.auth_token);
                        sessionStorage.setItem("auth_token", response.auth_token);
                        this.$router.push({name: "home"})
                    },
                    error: (response) => {
                        if (response.status === 400){
                            alert("Неверный логин или пароль!")
                        }
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>
