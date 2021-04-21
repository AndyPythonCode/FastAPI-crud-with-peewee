<template>
  <div v-if="book" class="d-inline">
    <!-- Button trigger modal -->
    <button
      type="button"
      :class="color"
      data-bs-toggle="modal"
      :data-bs-target="`#book-update-${book.id}`"
    >
      <i :class="icon"></i>
    </button>

    <!-- Modal -->
    <div
      class="modal fade"
      :id="`book-update-${book.id}`"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header mx-auto">
            <h5 class="modal-title" id="exampleModalLabel">Updating</h5>
          </div>
          <div class="modal-body">
            <!--FORM-->
            <!--INPUT-->
            <div v-for="item in form" :key="item" class="input-group mb-3">
              <div class="input-group-text">
                <i :class="item.icon"></i>
              </div>
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
            <!--INPUT-->
            <!--FORM-->
          </div>

          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
              @click="reset()"
            >
              Close
            </button>
            <button
              @click="update()"
              data-bs-dismiss="modal"
              class="btn btn-warning"
            >
              Update
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch } from "vue";
import BookForm from "../../assets/book/BookForm";
import updateBook from "../../composables/updateBook";

export default {
  name: "BookUpdate",
  props: {
    icon: String,
    color: String,
    load: Function,
    book: Object,
  },
  setup(props) {
    const { icon, color, load, book } = props;
    const form = BookForm;
    const { message, error, updating } = updateBook();
    const data = ref({
      id: book.id,
      title: book.title,
      body: book.body,
      price: book.price,
      is_offer: book.is_offer,
    });

    watch(
      () => [message.value, error.value],
      () => {
        message.value ? console.log(message.value) : console.log(error.value);
      }
    );

    function reset() {
      data.value.title = book.title;
      data.value.body = book.body;
      data.value.price = book.price;
      data.value.is_offer = book.is_offer;
    }

    function update() {
      updating(data.value, load);
    }

    //show variable
    return {
      icon,
      color,
      book,
      form,
      data,
      reset,
      update,
    };
  },
};
</script>
