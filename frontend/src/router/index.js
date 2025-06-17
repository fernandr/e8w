import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import PersonList from '../components/PersonList.vue';
import AddPerson from '../components/AddPerson.vue';
import EditPerson from '../components/EditPerson.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/persons', component: PersonList },
  { path: '/add', component: AddPerson },
  { path: '/edit/:name', component: EditPerson, props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;