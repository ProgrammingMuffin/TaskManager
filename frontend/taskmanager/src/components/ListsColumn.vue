<template>
	<div class="lists_container" >
		<div class="logo" >TaskManager</div>
		<div class="padding" ></div>
		<div class="your_list" >Your lists
			<button class="add_list_button" @click="triggerFetchLists" >+</button>
		</div>
		<list-entry v-for="list in lists" :key="list" :value="list" />
	</div>
</template>

<script>
import ListEntry from "./ListEntry";
import { baseUrl, listsUri, backendPort } from "../util/apiUtil";
import { mapState } from "vuex";

export default {
	name: "lists-column",
	data () {
		return {
			lists: []
		}
	},
	components: {
		ListEntry
	},
	created () {
		this.getLists();	
	},
	computed: {
		...mapState(['fetch_lists'])
	},
	watch: {
		fetch_lists () {
			if (this.fetch_lists == 1) {
				console.log("fetching lists");
				this.lists.length = 0;
				this.getLists()
				this.$store.commit('stop_fetch_lists');
			} else {
				console.log("stopping fetch lists");
			}
		}
	},
	methods: {
		getLists () {
			fetch("http://" + baseUrl + backendPort + listsUri)
			.then((res) => { return res.json(); })
			.then((data) => {
				data.lists.forEach((list) => {
					this.lists.push(list.name);
				});
			})
			.catch((error) => { console.log(error); });
		},
		triggerFetchLists () {
			this.$store.commit('trigger_fetch_lists');
			this.$router.push('/list/create');
		}
	}

}
</script>

<style lang="scss" >

@import "../assets/stylesheets/base";

.lists_container {
	background-color: $primary_color;
	color: $secondary_color;
	width: 100vw * (25 / 100);
	min-height: 100vh;
	float:left;
}

.logo {
	background: inherit;
	color: $secondary_color;
	width: 100%;
	height: 50px;
	line-height: 50px;
	font-size: 30px;
	text-align: center;
	font-family: 'Pacifico', sans-serif;
	margin-top: 50px;
}

.your_list {
	background-color: $primary_color_dark_1;
	color: white;
	width: 100%;
	height: 40px;
	text-align: center;
	padding-top: 25px;
	padding-bottom: 25px;
	line-height: 40px;
	font-size: 20px;
	font-family: 'Roboto', sans-serif;
}

.padding {
	background: inherit;
	width: 100%;
	height: 75px;
}

.add_list_button {
	background: inherit;
	color: white;
	font-size: 40px;
	width: 40px;
	height: 40px;
	float: right;
	margin-right: 15px;
	text-align: center;
	line-height: 40px;
	outline: none;
	border: none
}

</style>
