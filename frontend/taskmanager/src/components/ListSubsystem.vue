<template>
	<div class="base_container" >
		<div>
			<lists-column></lists-column>
			<div class="routed_container" >
				<router-view></router-view>
			</div>
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
	max-width: 100%;
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

.routed_container {
	background: white;
	color: black;
	width: 75%;
	height: 100vh;
	float: left;
}
</style>
