<template>
	<div class="lists_container" >
		Testing 123
	</div>
</template>

<script>
export default {
	name: "lists-column",
	data () {
		return {}
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
