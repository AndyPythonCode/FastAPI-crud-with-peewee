<template>
  <div class="d-inline">
    <!-- Button trigger modal -->
    <button
      type="button"
      class="btn btn-secondary"
      data-bs-toggle="modal"
      data-bs-target="#book-body"
    >
      <i class="fas fa-align-justify"></i>
    </button>

    <!-- Modal -->
    <div
      class="modal fade"
      id="book-body"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header mx-auto">
            <h5 class="modal-title" id="exampleModalLabel">Body</h5>
          </div>
          <div class="modal-body">
            <div class="form-floating">
              <textarea
                ref="area"
                class="form-control"
                @keyup="writing"
                id="floatingTextarea"
              ></textarea>
              <label for="floatingTextarea">Content</label>
            </div>
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
import { computed, ref, watchEffect } from "vue";
export default {
  name: "BookBody",
  props: {
    body: Function,
    data: Object,
  },
  setup(props) {
    const input = computed(() => props.data.body.length);
    const area = ref({});

    watchEffect(() => {
      if (input.value == 0) {
        area.value.value = "";
      }
    });

    function writing(event) {
      props.body(event.target.value);
    }

    //Show variable
    return {
      writing,
      area,
    };
  },
};
</script>

<style>
#floatingTextarea {
  height: 500px;
}
</style>