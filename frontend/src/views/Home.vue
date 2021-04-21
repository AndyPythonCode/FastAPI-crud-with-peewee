<template>
  <GradientTop />
  <div class="container">
    <div class="row">
      <!--TABLE-->
      <div class="col-md-8">
        <BookTable :books="books" :load="load" />
      </div>
      <div class="col-md-4">
        <div class="row text-center">
          <!--FILTER-->
          <div class="col-md-12">
            <BookFilter :searcher="searcher" />
          </div>
          <!--ADD NEW-->
          <div class="col-md-12 mt-4">
            <BookCreate :load="load" />
          </div>
        </div>
      </div>
    </div>
  </div>
  <GradientBottom />
</template>

<script>
import GradientTop from "../components/Common/GradientTop";
import GradientBottom from "../components/Common/GradientBottom";
import BookTable from "../components/Books/BookTable";
import BookFilter from "../components/Books/BookFilter";
import BookCreate from "../components/Books/BookCreate";
import { computed, onMounted, ref } from "vue";
import getBooks from "../composables/getBooks";

export default {
  name: "Home",
  components: {
    BookTable,
    GradientTop,
    GradientBottom,
    BookFilter,
    BookCreate,
  },
  setup() {
    const { data, load } = getBooks();
    const searching = ref("");

    onMounted(() => {
      load();
    });

    const books = computed(() =>
      data.value.filter(
        (element) =>
          element.title.toLowerCase().includes(searching.value.toLowerCase()) ||
          element.price.toString().includes(searching.value)
      )
    );

    //EVENT FILTER
    function searcher(word) {
      searching.value = word;
    }

    //Show variable
    return {
      books,
      searcher,
      load,
    };
  },
};
</script>
