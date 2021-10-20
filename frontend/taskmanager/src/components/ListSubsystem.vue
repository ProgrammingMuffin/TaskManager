<template>
	<div class="base_container" >
		<div>
			<lists-column></lists-column>
		</div>
	</div>
</template>

<script>
import ListsColumn from "./ListsColumn";

export default {
	name: "list-subsystem",
	data () {
		return {}
	},
	components: {
		ListsColumn
	}
}
</script>

<style lang="scss" >

@import "../assets/stylesheets/base";

.base_container {
	background-color: $secondary_color;
	color: $accent;
	width: $screen_width;
	height: 100vh;
	margin-left: auto;
	margin-right: auto;
}

.base_container > div {
	background: inherit;
	min-width: $screen_width;
	width: 100%;
	min-height: 100vh;
	margin-left: auto;
	margin-right: auto;
}
</style>
