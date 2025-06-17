<template>
  <section aria-labelledby="edit-heading">
    <h2 id="edit-heading">Persoon bewerken: {{ route.params.name }}</h2>
    <form @submit.prevent="editPerson" class="rijk-form">
      <div class="form-group">
        <label for="name">Naam:</label>
        <input id="name" v-model="name" required autocomplete="name" />
      </div>
      <div class="form-group">
        <label for="email">E-mail:</label>
        <input id="email" v-model="email" required autocomplete="email" type="email" />
      </div>
      <button type="submit" class="rijk-btn">Opslaan</button>
    </form>
    <div v-if="message" role="status" aria-live="polite">{{ message }}</div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';

const route = useRoute();
const name = ref(route.params.name);
const email = ref('');
const message = ref('');

onMounted(async () => {
  const res = await axios.get('http://localhost:5000/api/persons');
  const person = res.data.find(p => p.name === route.params.name);
  if (person) {
    name.value = person.name;
    email.value = person.email;
  }
});

const editPerson = async () => {
  try {
    await axios.post(`http://localhost:5000/api/person/${route.params.name}`, { name: name.value, email: email.value });
    message.value = 'Persoon bijgewerkt!';
  } catch (e) {
    message.value = 'Fout bij bijwerken persoon.';
  }
};
</script>

<style scoped>
.rijk-form {
  max-width: 400px;
  background: #fff;
  padding: 1.5rem;
  border: 1px solid #00337f;
  border-radius: 4px;
}
.form-group {
  margin-bottom: 1rem;
}
label {
  display: block;
  font-weight: bold;
  margin-bottom: 0.3rem;
  color: #00337f;
}
input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #00337f;
  border-radius: 3px;
  font-size: 1rem;
}
input:focus {
  outline: 2px solid #ffd200;
}
.rijk-btn {
  background: #ffd200;
  color: #00337f;
  border: none;
  padding: 0.5rem 1.2rem;
  font-weight: bold;
  border-radius: 3px;
  cursor: pointer;
  transition: background 0.2s;
}
.rijk-btn:focus, .rijk-btn:hover {
  background: #ffe066;
  outline: 2px solid #00337f;
}
</style>