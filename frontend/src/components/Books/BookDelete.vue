<template>
  <div v-if="book" class="d-inline">
    <!-- Button trigger modal -->
    <button
      type="button"
      :class="color"
      data-bs-toggle="modal"
      :data-bs-target="`#book-delete-${book.id}`"
    >
      <i :class="icon"></i>
    </button>

    <!-- Modal -->
    <div
      class="modal fade"
      :id="`book-delete-${book.id}`"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div v-if="book" class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header mx-auto">
            <h5 class="modal-title" id="exampleModalLabel">Deleting</h5>
          </div>
          <div class="modal-body">
            <p class="fw-bold text-center">
              Are you sure you want to delete the selected item?
            </p>
          </div>

          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Close
            </button>
            <button
              @click="getDeleteBook(book)"
              data-bs-dismiss="modal"
              class="btn btn-danger"
            >
              Delete
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { watch } from "vue";
import deleteBook from "../../composables/deleteBook";

export default {
  name: "BookDelete",
  props: {
    icon: String,
    color: String,
    load: Function,
    book: Object,
  },
  setup(props) {
    const { icon, color, load, book } = props;
    const { message, error, delBook } = deleteBook();

    watch(
      () => [message.value, error.value],
      () => {
        message.value ? console.log(message.value) : console.log(error.value);
      }
    );

    function getDeleteBook(book) {
      delBook(book.id, load);
    }

    //show variable
    return {
      icon,
      color,
      book,
      getDeleteBook,
    };
  },
};
</script>
