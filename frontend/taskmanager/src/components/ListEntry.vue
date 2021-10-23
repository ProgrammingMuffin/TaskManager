<template>
	<div class="list_entry" >
		<img src="../assets/list.png" class="list_image" />
		<div class="list_text" >{{ value }}</div>
	</div>
</template>

<script>
export default {
	name: "list-entry",
	data () {
		return {}
	},
	props: [
		"value"
	]
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
	color: white;
	padding-left: 15px;
	line-height: 35px;
	vertical-align: middle;
	float: left;
	font-size: 18px;
	font-family: 'Roboto', sans-serif;
}
</style>
