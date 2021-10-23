import { createRouter, createWebHistory } from "vue-router"
import ListCreate from "./components/ListCreate"

export const router = createRouter({
	history: createWebHistory(),
	routes: [
		{ path: '/list/create', component: ListCreate }
	]
});
