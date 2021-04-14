<template>
  <div class="home">
    <ListBook uno="uno" />
  </div>
</template>

<script>
import ListBook from "./books/ListBook";
export default {
  name: "Home",
  components: {
    ListBook,
  },
};
</script>
