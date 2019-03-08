<template>
    <div>
        <h1>Kanban Board</h1>
        <button v-if="!authorized" @click="goLogin">Вход</button>
        <button v-else @click="logout">Выход</button>
        <KanbanBoard></KanbanBoard>
    </div>
</template>

<script>
    import KanbanBoard from "@/components/KanbanBoard";

    export default {
        name: "Home",
        components: {
            KanbanBoard
        },
        computed: {
            authorized() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods: {
            goLogin() {
                this.$router.push({name: "login"})
            },
            logout() {
                sessionStorage.removeItem("auth_token");
                window.location = "/"
            }
        }
    }
</script>

<style src="../style.css"/>
