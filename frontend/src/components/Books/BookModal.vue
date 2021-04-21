<template>
  <div v-if="book" class="d-inline">
    <!-- Button trigger modal -->
    <button
      type="button"
      :class="color"
      data-bs-toggle="modal"
      :data-bs-target="`#book-show-${book.id}`"
    >
      <i :class="icon"></i>
    </button>

    <!-- Modal -->
    <div
      class="modal fade"
      :id="`book-show-${book.id}`"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header mx-auto">
            <h5 class="modal-title" id="exampleModalLabel">{{ book.title }}</h5>
          </div>
          <div class="modal-body">
            <p class="fw-bold text-center">
              Price: ${{ book.price }}
              <span class="fw-bold" v-if="book.is_offer">| Offer: Yes</span>
              <span class="fw-bold" v-else>| Offer: No</span>
            </p>
            <!--BODY-->
            <div class="card text-center">
              <div class="card-header">Content</div>
              <div class="card-body">
                <p class="card-text">
                  {{ book.body }}
                </p>
              </div>
            </div>
            <!--BODY-->
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BookModal",
  props: {
    icon: String,
    color: String,
    book: Object,
  },
  setup(props) {
    const { icon, color, book } = props;

    //show value
    return {
      icon,
      color,
      book,
    };
  },
};
</script>