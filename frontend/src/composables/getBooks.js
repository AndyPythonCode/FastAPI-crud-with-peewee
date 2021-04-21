import { ref } from "vue";
import axios from "axios";

const getBooks = () => {
  const data = ref([]);
  const error = ref("");

  const load = async () => {
    try {
      //can use try catch for errors
      const response = await axios.get(
        `${process.env.VUE_APP_API_BASE}/books/`
      );
      data.value = await response.data;
    } catch (err) {
      error.value = err;
    }
  };

  return { data, error, load };
};

export default getBooks;
