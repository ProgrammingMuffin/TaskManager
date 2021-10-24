<template>
	<list-window :title="selected_list.name" >
		<button class="red_button" @click="deleteList" >Delete</button>	
	</list-window>
</template>

<script>
import ListWindow from "./ListWindow";
import { baseUrl, listsUri, backendPort } from "../util/apiUtil";
import { mapState } from "vuex";

export default {
	name: 'list-selected',
	data () {
		return {}
	},
	computed: {
		...mapState(['selected_list'])
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
			
		}
	},
	components: {
		ListWindow
	}
}
</script>

<style lang="scss" >
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
