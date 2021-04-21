<template>
  <div class="card">
    <div class="card-header bg">Create books</div>
    <div class="card-body">
      <form @submit.prevent="createBook()" action="">
        <!--Show message send-->
        <span v-if="send">
          <Message
            content="You added a new one"
            color="success"
            :active="addedNewOne"
        /></span>
        <span v-if="error">
          <Message
            content="The first three are required"
            color="danger"
            :active="notAddedNewOne"
        /></span>
        <!--Show message send-->

        <!--INPUT-->
        <div v-for="item in form" :key="item" class="input-group mb-3">
          <!--BOOK BODY CONTAINER-->
          <div v-if="item.name != 'body'" class="input-group-text">
            <i :class="item.icon"></i>
          </div>
          <BookBody v-else :body="body" :data="data" />
          <input
            :name="item.name"
            :type="item.type"
            :class="item.class"
            :placeholder="item.placeholder"
            class="mx-auto text-center"
            step="0.1"
            min="0"
            v-model="data[item.name]"
          />
        </div>
        <div class="d-grid mb-3">
          <button class="btn btn-outline-primary" type="submit">New one</button>
        </div>
        <!--INPUT-->
      </form>
      <blockquote class="blockquote mb-0">
        <footer class="blockquote-footer">
          <cite title="Source Title">Add new books</cite>
        </footer>
      </blockquote>
    </div>
  </div>
</template>

<style>
.bg {
  color: black;
  font-weight: 750;
}
</style>

<script>
import { ref } from "vue";
import BookForm from "../../assets/book/BookForm.js";
import Message from "../Common/Message";
import axios from "axios";
import BookBody from "./BookBody";

export default {
  name: "BookCreate",
  components: {
    Message,
    BookBody,
  },
  props: {
    load: Function,
  },
  setup(props) {
    const form = BookForm;
    const send = ref(false);
    const error = ref(false);

    const data = ref({
      title: "",
      body: "",
      price: "",
      is_offer: false,
    });

    function body(variable) {
      data.value.body = variable;
    }

    //Message
    function addedNewOne() {
      send.value = !send.value;
      data.value.title = "";
      data.value.body = "";
      data.value.price = "";
      data.value.is_offer = false;
    }

    function notAddedNewOne() {
      error.value = !error.value;
    }

    //Create
    async function createBook() {
      try {
        await axios.post(`${process.env.VUE_APP_API_BASE}/books/`, data.value);
        addedNewOne();
        props.load();
      } catch (error) {
        console.log(error.response);
        notAddedNewOne();
      }
    }
    //Show variable
    return {
      form,
      data,
      send,
      addedNewOne,
      error,
      notAddedNewOne,
      createBook,
      body,
    };
  },
};
</script>
