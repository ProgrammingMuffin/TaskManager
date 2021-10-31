<template>
	<list-window :title="selected_list.name" >
		<task-entry v-for="task in tasks" :key="task" :task="task" ></task-entry>
		<button class="red_button" @click="deleteList" >Delete</button>	
	</list-window>
</template>

<script>
import ListWindow from "./ListWindow";
import { baseUrl, listsUri, backendPort, tasksUri } from "../util/apiUtil";
import { mapState } from "vuex";
import TaskEntry from './TaskEntry.vue';

export default {
	name: 'list-selected',
	data () {
		return {
			tasks: []
		}
	},
	computed: {
		...mapState(['selected_list'])
	},
	created () {
		this.getTasks()
	},
	methods: {
		deleteList: function () {
			fetch("http://" + baseUrl + backendPort + listsUri +
			"/" + this.selected_list.id, {
				method: "DELETE"
			})
			.then((res) => { return res.json(); })
			.then((data) => {
				if (data.message.includes("List deleted")) {
					this.$store.commit('trigger_fetch_lists')
					this.$router.push('/list/create')
					console.log("deleted");
				}
			})
			.catch((error) => { console.log(error); });
			
		},
		getTasks: function () {
			fetch("http://" + baseUrl + backendPort + listsUri +
			"/" + this.selected_list.id + tasksUri, {
				method: "GET"
			})
			.then((res) => { return res.json(); })
			.then((data) => {
				this.tasks = data
				console.log("tasks fetched successfully")
			})
			.catch((error) => { console.log(error); });
		}
	},
	components: {
		ListWindow,
		TaskEntry
	}
}
</script>


TaskEntry<style lang="scss" >
@import "../assets/stylesheets/base";

.red_button {
	padding: 5px;
	background-color: $warning_red;
	color: $secondary_color;
	width: 15%;
	height: 35px;
	font-family: 'Roboto', sans-serif;
	font-size: 18px;
	display: block;
	margin-left: auto;
	margin-right: auto;
	margin-top: 15px;
	margin-bottom: 15px;
	border: none;
	outline: none; 
}

.red_button:hover {
	background-color: $warning_red_dark_1;
}
</style>
