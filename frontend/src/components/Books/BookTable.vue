<template>
  <div id="myTable" class="overflow-auto">
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">title</th>
          <th scope="col">body</th>
          <th scope="col">price</th>
          <th scope="col">offer</th>
          <th scope="col">option</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(book, index) in books" :key="book.id">
          <th scope="row">{{ index + 1 }}</th>
          <td>{{ book.title }}</td>
          <td>{{ showSomeWords(book.body) }}</td>
          <td>$ {{ book.price }}</td>
          <td v-if="book.is_offer == true">Yes</td>
          <td v-else>No</td>
          <td>
            <BookModal
              icon="far fa-eye"
              color="btn btn-primary me-1 btn-sm"
              :book="book"
            />
            <BookUpdate
              icon="far fa-edit"
              color="btn btn-warning me-1 btn-sm"
              :book="book"
              :load="load"
            />
            <BookDelete
              icon="far fa-trash-alt"
              color="btn btn-danger btn-sm"
              :book="book"
              :load="load"
            />
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style>
#myTable {
  height: 525px;
}
</style>

<script>
import { computed } from "vue";
import BookModal from "./BookModal";
import BookDelete from "./BookDelete";
import BookUpdate from "./BookUpdate";

export default {
  name: "BookTable",
  components: {
    BookModal,
    BookDelete,
    BookUpdate,
  },
  props: {
    books: Array,
    load: Function,
  },

  setup(props) {
    const books = computed(() => props.books);

    function showSomeWords(body) {
      return `${body.substring(0, 17)}...`;
    }

    //show value
    return { books, showSomeWords, load: props.load };
  },
};
</script>