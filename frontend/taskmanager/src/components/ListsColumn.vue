<template>
	<div class="lists_container" >
		<list-entry v-for="list in lists" :key="list" :value="list" />
	</div>
</template>

<script>
import ListEntry from "./ListEntry";
import { baseUrl, listsUri } from "../util/apiUtil";

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
	mounted () {
		this.getLists();	
	},
	methods: {
		getLists: () => {
			fetch("http://" + baseUrl + listsUri)
			.then((res) => { this.$data.lists.append(res.body); })
			.catch((error) => { console.log(error); })
		}
	}
}
</script>

<style lang="scss" >

@import "../assets/stylesheets/base";

.lists_container {
	background-color: $primary_color;
	color: $secondary_color;
	width: $screen_width * (40 / 100);
	min-height: 100vh;
	float:left;
}

</style>
