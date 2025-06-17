<template>
  <section aria-labelledby="personen-heading">
    <h2 id="personen-heading">Personen</h2>
    <table class="rijk-table">
      <thead>
        <tr>
          <th scope="col">Naam</th>
          <th scope="col">E-mail</th>
          <th scope="col">Acties</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="person in persons" :key="person.id">
          <td>{{ person.name }}</td>
          <td>{{ person.email }}</td>
          <td>
            <router-link :to="`/edit/${person.name}`" class="rijk-btn">Bewerken</router-link>
            <button @click="deletePerson(person.name)" class="rijk-btn rijk-btn-delete" aria-label="Verwijder {{ person.name }}">Verwijderen</button>
          </td>
        </tr>
      </tbody>
    </table>
    <div v-if="message" role="status" aria-live="polite">{{ message }}</div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const persons = ref([]);
const message = ref('');

const fetchPersons = async () => {
  const res = await axios.get('http://localhost:5000/api/persons');
  persons.value = res.data;
};

onMounted(fetchPersons);

const deletePerson = async (name) => {
  if (!confirm(`Weet u zeker dat u ${name} wilt verwijderen?`)) return;
  try {
    await axios.delete(`http://localhost:5000/api/person/${encodeURIComponent(name)}`);
    message.value = `Persoon ${name} verwijderd.`;
    await fetchPersons();
  } catch (e) {
    message.value = `Fout bij verwijderen van ${name}.`;
  }
};
</script>

<style scoped>
.rijk-table {
  width: 100%;
  border-collapse: collapse;
  background: #fff;
  color: #1e1e1e;
}
.rijk-table th, .rijk-table td {
  border: 1px solid #00337f;
  padding: 0.5rem 1rem;
  text-align: left;
}
.rijk-table th {
  background: #00337f;
  color: #fff;
}
.rijk-btn {
  background: #ffd200;
  color: #00337f;
  border: none;
  padding: 0.3rem 1rem;
  text-decoration: none;
  font-weight: bold;
  border-radius: 3px;
  transition: background 0.2s;
  margin-right: 0.5rem;
  cursor: pointer;
}
.rijk-btn:focus, .rijk-btn:hover {
  background: #ffe066;
  outline: 2px solid #00337f;
}
.rijk-btn-delete {
  background: #e03131;
  color: #fff;
}
.rijk-btn-delete:focus, .rijk-btn-delete:hover {
  background: #c92a2a;
  outline: 2px solid #00337f;
}
</style>