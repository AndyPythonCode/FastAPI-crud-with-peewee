import axios from "axios";
import { ref } from "vue";

const updateBook = () => {
  const message = ref({});
  const error = ref({});

  const updating = async (book, load) => {
    try {
      const response = await axios.put(
        `${process.env.VUE_APP_API_BASE}/books/${book.id}`,
        {
          title: book.title,
          body: book.body,
          price: book.price,
          is_offer: book.is_offer,
        }
      );
      message.value = response.data;
      load();
    } catch (err) {
      error.value = err;
    }
  };

  return { message, error, updating };
};

export default updateBook;
