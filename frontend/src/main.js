import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
//Bootstrap 5 reduce
import "./assets/scss/custom.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
// import "./assets/scss/reduce.css"; when deploy

createApp(App)
  .use(router)
  .mount("#app");
