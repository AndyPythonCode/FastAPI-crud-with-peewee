<template>
  <div class="gradientsTop">
    <p class="pt-2">
      API LIBRARY
      <i class="ms-1 fas fa-book-reader"></i>
    </p>
  </div>
</template>

<script>
export default {
  name: "GradientTop",
};
</script>

<style>
.gradientsTop {
  background: #00f260; /* fallback for old browsers */
  background: -webkit-linear-gradient(
    to right,
    #0575e6,
    #00f260
  ); /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(
    to right,
    #0575e6,
    #00f260
  ); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  height: 80px;
  margin-bottom: 1.5rem;
  box-shadow: 1px 13px 16px -6px rgba(0, 0, 0, 0.25);
  -webkit-box-shadow: 1px 13px 16px -6px rgba(0, 0, 0, 0.25);
  -moz-box-shadow: 1px 13px 16px -6px rgba(0, 0, 0, 0.25);
  text-align: center;
  color: #fff;
  font-weight: 800;
  font-size: 2rem;
}
</style>