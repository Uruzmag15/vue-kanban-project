<template>
    <div class="kanban-board">
        <div class="row">
            <h3 class="header orange">On Hold ({{items0.length}})</h3>
            <Container :group-name="'1'" :get-child-payload="getChildPayload0" @drop="onDrop('items0', $event, 'on hold')">
                <Draggable v-for="item in items0" :key="item.id">
                    <div class="draggable-item">
                        <div class="delete" @click="deleteItem(item)"></div>
                        <p><b class="id">id: </b>{{item.id}}</p>
                        <p>text: {{item.text}}</p>
                        <p>status in DB: "{{item.status}}"</p>
                    </div>
                </Draggable>
            </Container>
            <textarea id="title0" class="card-title-textarea" rows="5" placeholder="Ввести заголовок для этой карточки" v-model="newCardHeader" v-bind:style="addACardStyle[0]"></textarea>
            <button class="add-a-card" @click="addItem('on hold')" v-bind:style="addACardStyle[0]">Добавить карточку</button>
            <button class="cancel" @click="hideAddACardTextarea()" v-bind:style="addACardStyle[0]"></button>
            <button class="add-another-card" @click="showAddACardTextarea(0)" v-bind:style="addAnotherCardStyle[0]">Добавить карточку</button>
        </div>
        <div class="row">
            <h3 class="header blue">In Progress ({{items1.length}})</h3>
            <Container :group-name="'1'" :get-child-payload="getChildPayload1" @drop="onDrop('items1', $event, 'in progress')">
                <Draggable v-for="item in items1" :key="item.id">
                    <div class="draggable-item">
                        <div class="delete" @click="deleteItem(item)"></div>
                        <p><b class="id">id: </b>{{item.id}}</p>
                        <p>text: {{item.text}}</p>
                        <p>status in DB: "{{item.status}}"</p>
                    </div>
                </Draggable>
            </Container>
            <textarea id="title1" class="card-title-textarea" rows="5" placeholder="Ввести заголовок для этой карточки" v-model="newCardHeader" v-bind:style="addACardStyle[1]"></textarea>
            <button class="add-a-card" @click="addItem('in progress')" v-bind:style="addACardStyle[1]">Добавить карточку</button>
            <button class="cancel" @click="hideAddACardTextarea()" v-bind:style="addACardStyle[1]"></button>
            <button class="add-another-card" @click="showAddACardTextarea(1)" v-bind:style="addAnotherCardStyle[1]">Добавить карточку</button>
        </div>
        <div class="row">
            <h3 class="header yellow">Needs Review ({{items2.length}})</h3>
            <Container :group-name="'1'" :get-child-payload="getChildPayload2" @drop="onDrop('items2', $event)">
                <Draggable v-for="item in items2" :key="item.id">
                    <div class="draggable-item">
                        <div class="delete" @click="deleteItem(item)"></div>
                        <p><b class="id">id: </b>{{item.id}}</p>
                        <p>text: {{item.text}}</p>
                        <p>status in DB: "{{item.status}}"</p>
                    </div>
                </Draggable>
            </Container>
            <textarea id="title2" class="card-title-textarea" rows="5" placeholder="Ввести заголовок для этой карточки" v-model="newCardHeader" v-bind:style="addACardStyle[2]"></textarea>
            <button class="add-a-card" @click="addItem('needs review')" v-bind:style="addACardStyle[2]">Добавить карточку</button>
            <button class="cancel" @click="hideAddACardTextarea()" v-bind:style="addACardStyle[2]"></button>
            <button class="add-another-card" @click="showAddACardTextarea(2)" v-bind:style="addAnotherCardStyle[2]">Добавить карточку</button>
        </div>
        <div class="row">
            <h3 class="header green">Approved ({{items3.length}})</h3>
            <Container :group-name="'1'" :get-child-payload="getChildPayload3" @drop="onDrop('items3', $event)">
                <Draggable v-for="item in items3" :key="item.id">
                    <div class="draggable-item">
                        <div class="delete" @click="deleteItem(item)"></div>
                        <p><b class="id">id: </b>{{item.id}}</p>
                        <p>text: {{item.text}}</p>
                        <p>status in DB: "{{item.status}}"</p>
                    </div>
                </Draggable>
            </Container>
            <textarea id="title3" class="card-title-textarea" rows="5" placeholder="Ввести заголовок для этой карточки" v-model="newCardHeader" v-bind:style="addACardStyle[3]"></textarea>
            <button class="add-a-card" @click="addItem('approved')" v-bind:style="addACardStyle[3]">Добавить карточку</button>
            <button class="cancel" @click="hideAddACardTextarea()" v-bind:style="addACardStyle[3]"></button>
            <button class="add-another-card" @click="showAddACardTextarea(3)" v-bind:style="addAnotherCardStyle[3]">Добавить карточку</button>
        </div>
    </div>
</template>

<script>
    import { Container, Draggable } from "vue-smooth-dnd";
    import { applyDrag, saveItems } from "./my_utils";

    export default {
        name: "KanbanBoard",
        components: { Container, Draggable },
        data() {
            return {
                items0: "",
                items1: "",
                items2: "",
                items3: "",
                newCardHeader: '',
                addACardStyle: [
                    { display: 'none'},
                    { display: 'none'},
                    { display: 'none'},
                    { display: 'none'}
                ],
                addAnotherCardStyle: [
                    { display: 'block'},
                    { display: 'block'},
                    { display: 'block'},
                    { display: 'block'}
                ]
            };
        },
        created() {
            if (sessionStorage.getItem("auth_token")) {
                $.ajaxSetup({
                    headers: {"Authorization": "Token " + sessionStorage.getItem("auth_token")},
                });
            }
            this.updateBoardData()
        },
        methods: {
            loadCards(collection, status) {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/kanban/card/",
                    type: "GET",
                    data: {
                        status: status
                    },
                    success: (response) => {
                        this[collection] = response;
                    },
                })
            },
            addNewCard(status) {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/kanban/card/add/",
                    type: "POST",
                    data: {
                        status: status,
                        text: this.newCardHeader
                    },
                    success: (response) => {
                        this.updateBoardData(status)
                    },
                    error: (response) => {
                        alert(response.statusText)
                    }
                })
            },
            deleteCard(card) {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/kanban/card/delete/",
                    type: "GET",
                    data: {
                        card_id: card.id
                    },
                    success: (response) => {
                        this.updateBoardData(card.status)
                    },
                    error: (response) => {
                        alert(response.statusText)
                    }
                })
            },
            updateBoardData(status) {
                switch (status) {
                    case "on hold":
                        this.loadCards("items0", status);
                        break;
                    case "in progress":
                        this.loadCards("items1", status);
                        break;
                    case "needs review":
                        this.loadCards("items2", status);
                        break;
                    case "approved":
                        this.loadCards("items3", status);
                        break;
                    default:
                        this.loadCards("items0", "on hold");
                        this.loadCards("items1", "in progress");
                        this.loadCards("items2", "needs review");
                        this.loadCards("items3", "approved");
                }
            },
            onDrop: function(collection, dropResult) {
                this.hideAddACardTextarea();
                this[collection] = applyDrag(this[collection], dropResult);
                saveItems(collection, this[collection])
            },
            // onDrop: function(collection, dropResult, status) {
            //     this.hideAddACardTextarea();
            //     this[collection] = applyDrag(this[collection], dropResult);
            //     saveItems(collection, this[collection]);
            //     this.updateBoardData();
            // },
            getChildPayload0: function(index) {
                return this.items0[index];
            },
            getChildPayload1: function(index) {
                return this.items1[index];
            },
            getChildPayload2: function(index) {
                return this.items2[index];
            },
            getChildPayload3: function(index) {
                return this.items3[index];
            },
            // addItem: function(collection) {
            //     if (this.newCardHeader) {
            //         const d = new Date();
            //         const newID = d.getTime();
            //         this[collection].push({ id: newID, header: this.newCardHeader });
            //         saveItems(collection, this[collection]);
            //         this.hideAddACardTextarea();
            //     }
            // },
            addItem: function(status) {
                if (this.newCardHeader) {
                    this.addNewCard(status);
                    this.hideAddACardTextarea();
                }
            },
            // deleteItem: function(collection, item) {
            //     let index = this[collection].map(x => {
            //         return x.id;
            //     }).indexOf(item.id);
            //     this[collection].splice(index, 1);
            //     saveItems(collection, this[collection]);
            // },
            deleteItem: function(item) {
                if (sessionStorage.getItem("auth_token")) {
                    this.deleteCard(item);
                }
                else alert("Авторизуйтесь для удаления карточек!")
            },
            hideAddACardTextarea: function() {
                this.newCardHeader = '';
                for(let i = 0; i < this.addACardStyle.length; i++) {
                    this.addACardStyle[i].display = 'none';
                }
                for(let i = 0; i < this.addAnotherCardStyle.length; i++) {
                    this.addAnotherCardStyle[i].display = 'block';
                }
            },
            showAddACardTextarea: function(col) {
                if (sessionStorage.getItem("auth_token")) {
                    this.hideAddACardTextarea();
                    this.addAnotherCardStyle[col].display = 'none';
                    this.addACardStyle[col].display = 'block';
                    let textareaID = 'title' + col;

                    setTimeout(function() {
                        document.getElementById(textareaID).focus();
                    }, 0);
                }
                else alert("Авторизуйтесь для добавления карточек!")

            }
        }
    };
</script>
