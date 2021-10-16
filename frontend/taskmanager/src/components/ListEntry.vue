<template>
	<div class="list_entry" >
		{{ value }}
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

.list_entry {
	background-color: $primary_color;
	color: $secondary_color;
	width: 100%;
	height: 40px;
	line-height: 40px;
	text-align: center;
}
</style>
