<template>
  <div>
    <p v-for="element in data" :key="element">{{ element }}</p>
  </div>
</template>

<script>
import { ref, watchEffect } from "vue";
import axios from "axios";

export default {
  setup() {
    const data = ref(null);

    watchEffect(() => {
      listBooks();
    });

    function listBooks() {
      axios
        .get(`http://127.0.0.1:8000/books/5`)
        .then((res) => {
          data.value = res.data;
        })
        .catch((error) => {
          console.log(error.response.data.message);
        });
    }

    //variable visible
    return {
      data,
    };
  },
};
</script>