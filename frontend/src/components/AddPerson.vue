<template>
  <section aria-labelledby="add-heading">
    <h2 id="add-heading">Persoon toevoegen</h2>
    <form @submit.prevent="addPerson" class="rijk-form">
      <div class="form-group">
        <label for="name">Naam:</label>
        <input id="name" v-model="name" required autocomplete="name" />
      </div>
      <div class="form-group">
        <label for="email">E-mail:</label>
        <input id="email" v-model="email" required autocomplete="email" type="email" />
      </div>
      <button type="submit" class="rijk-btn">Toevoegen</button>
    </form>
    <div v-if="message" role="status" aria-live="polite">{{ message }}</div>
  </section>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const name = ref('');
const email = ref('');
const message = ref('');

const addPerson = async () => {
  try {
    await axios.post('http://localhost:5000/api/person', { name: name.value, email: email.value });
    message.value = 'Persoon toegevoegd!';
    name.value = '';
    email.value = '';
  } catch (e) {
    message.value = 'Fout bij toevoegen persoon.';
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