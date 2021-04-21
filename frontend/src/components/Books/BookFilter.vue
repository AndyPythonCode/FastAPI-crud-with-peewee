<template>
  <div class="card mt-2">
    <div class="card-header bg">Filter books (title, price)</div>
    <div class="card-body">
      <!--INPUT-->
      <div class="input-group mb-3">
        <div class="input-group-text">
          <i class="fas fa-book"></i>
        </div>
        <input
          type="text"
          class="form-control text-center"
          aria-label="Text input with checkbox"
          placeholder="Waiting title...."
          v-model="input"
        />
      </div>
      <!--INPUT-->
      <blockquote class="blockquote mb-0">
        <footer class="blockquote-footer">
          <cite title="Source Title">Look for famous titles</cite>
        </footer>
      </blockquote>
    </div>
  </div>
</template>

<script>
import { ref, watch } from "vue";
export default {
  name: "BookFilter",
  props: {
    searcher: Function,
  },
  setup(props) {
    const input = ref("");

    watch(
      () => [input.value],
      () => {
        input.value.length > 0
          ? props.searcher(input.value)
          : props.searcher("");
      }
    );
    //show variable
    return {
      input,
    };
  },
};
</script>