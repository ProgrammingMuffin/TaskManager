<template>
	<div v-bind:class="[current_list_selected ? 'list_entry_selected' : 'list_entry']" 
	@click="selectList" >
		<img src="../assets/list.png" class="list_image" />
		<div class="list_text" >{{ value }}</div>
	</div>
</template>

<script>
import { mapState } from "vuex";
export default {
	name: "list-entry",
	data () {
		return {
			current_list_selected: 0
		}
	},
	props: [
		"value",
		"list_id"
	],
	computed: {
		...mapState(['selected_list'])
	},
	watch: {
		selected_list () {
			if (this.list_id == this.$store.state.selected_list.id) {
				this.current_list_selected = 1;
			} else {
				this.current_list_selected = 0;
			}
		}
	},
	methods: {
		selectList: function () {
			this.$store.commit("select_list", {id: this.list_id, name: this.value});
			this.$router.push('/list/selected');
		}
	}
}
</script>

<style lang="scss" >
@import "../assets/stylesheets/base";
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.list_entry {
	background-color: $primary_color;
	color: $secondary_color;
	width: 100%;
	height: 35px;
	display: block;
	margin-top: 15px;
	cursor: pointer;
}

.list_entry_selected {
	background-color: $secondary_color;
	color: $accent;
	width: 100%;
	height: 35px;
	display: block;
	margin-top: 15px;
	cursor: pointer;
}

.list_image {
	background: inherit;
	width: 35px;
	height: 35px;
	display: block;
	float: left;
	padding-left: 15px;
}

.list_text {
	background: inherit;
	color: inherit;
	padding-left: 15px;
	line-height: 35px;
	vertical-align: middle;
	float: left;
	font-size: 18px;
	font-family: 'Roboto', sans-serif;
}

.list_entry:hover {
	background-color: $primary_color_dark_1;
}
</style>
