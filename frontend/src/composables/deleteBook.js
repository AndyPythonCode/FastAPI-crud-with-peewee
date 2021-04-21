import { ref } from "vue";
import axios from "axios";

const deleteBook = () => {
  const message = ref({});
  const error = ref({});

  const delBook = async (id, load) => {
    try {
      const response = await axios.delete(
        `${process.env.VUE_APP_API_BASE}/books/${id}`
      );
      message.value = await response.data;
      load();
    } catch (err) {
      error.value = err;
    }
  };
  return { message, error, delBook };
};

export default deleteBook;
