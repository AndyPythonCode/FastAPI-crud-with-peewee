<template>
  <div class="gradientsBottom"></div>
</template>

<script>
export default {
  name: "GradientBottom",
};
</script>

<style>
.gradientsBottom {
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
  height: 70px;
  position: block;
  margin-top: 60px;
  width: 100%;
}

@media (max-width: 768px) {
  .gradientsBottom {
    position: static;
    margin-top: 2rem;
  }
}
</style>