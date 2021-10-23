<template>
	<div class="list_window" >
		<div class="list_window_header" >{{ title }}</div>
		<slot></slot>
	</div>
</template>

<script>
export default {
	name: "list-window",
	props: [
		"title"
	],
	data () {
		return {}
	}
}
</script>

<style lang="scss" >

@import "../assets/stylesheets/base";

.list_window {
	width: 75%;
	border: 1px solid $primary_color;
	margin-left: auto;
	margin-right: auto;
	margin-top: 50px;
}

.list_window_header {
	width: 100%;
	margin: 0;
	padding-top: 5px;
	padding-bottom: 5px;
	background-color: $primary_color;
	color: $secondary_color;
	height: 30px;
	line-height: 30px;
	font-family: 'Roboto', sans-serif;
	text-align: center;
	font-weight: 600;
	font-size: 19px;
}

</style>
