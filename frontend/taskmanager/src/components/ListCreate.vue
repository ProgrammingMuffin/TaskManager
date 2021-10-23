<template>
	<list-window title="Create a new list" >
		<div>
			<div class="input_row" >
				<div class="label" >List name</div>
				<input type="text" v-model="list_name" />
			</div>
			<input type="submit" value="Create" @click="createList" />
		</div>
	</list-window>
</template>

<script>
import ListWindow from "./ListWindow";
import { baseUrl, listsUri, backendPort } from "../util/apiUtil";

export default {
	name: 'list-create',
	data () {
		return {
			list_name: ""
		}
	},
	methods: {
		createList: function () {
			let request_body = {
				"name": this.list_name,
				"recurring_deadline": "10:00:00"
			};
			fetch("http://" + baseUrl + backendPort + listsUri, {
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
				body: JSON.stringify(request_body) 
			})
			.then((res) => { return res.json(); })
			.then(() => {
					this.$store.commit('trigger_fetch_lists');
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

.input_row {
	background: inherit;
	width: 30%;
	margin-left: auto;
	margin-right: auto;
	margin-top: 30px;
	margin-bottom: 30px;
}

.label {
	background: inherit;
	color: $accent;
	font-family: 'Roboto', sans-serif;
	font-size: 18px;
	display: inline-block;
}

input[type="text"] {
	border: 2px solid $primary_color;
	color: $accent;
	width: 55%;
	height: 25px;
	padding: 2px;
	outline: none;
	font-family: 'Roboto', sans-serif;
	font-size: 18px;
	display: inline-block;
	margin-left: 50px;
}

input[type="submit"] {
	padding: 5px;
	background-color: $primary_color;
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

input[type="submit"]:hover {
	background-color: $primary_color_dark_1;
}
</style>
