<template>
  <div :class="`alert alert-${color} alert-dismissible fade show`" role="alert">
    <strong>{{ content }}</strong>
    <button
      type="button"
      class="btn-close"
      data-bs-dismiss="alert"
      aria-label="Close"
      @click="active"
    ></button>
  </div>
</template>

<script>
export default {
  name: "Message",
  props: {
    content: String,
    color: String,
    active: Function,
  },
  setup(props) {
    //Show variable
    return {
      content: props.content,
      color: props.color,
      active: props.active,
    };
  },
};
</script>