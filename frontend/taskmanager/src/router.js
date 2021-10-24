import { createRouter, createWebHistory } from "vue-router"
import ListCreate from "./components/ListCreate"
import ListSelected from "./components/ListSelected"

export const router = createRouter({
	history: createWebHistory(),
	routes: [
		{ path: '/list/create', component: ListCreate },
		{ path: '/list/selected', component: ListSelected }
	]
});
