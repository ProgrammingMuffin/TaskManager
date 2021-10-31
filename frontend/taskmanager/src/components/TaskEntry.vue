<template>
  <div class="task_entry" >
    <span class="task">
        {{ task.name }}
      <img src="../assets/check.png" class="mark_done_button" />
      <img src="../assets/trash.png" class="delete_button" />
    </span>
  </div>
</template>

<script>

export default {
    name: "task-entry",
    data () {
        return {}
    },
    props: [
        "task"
    ]
}
</script>

<style lang="scss">
@import "../assets/stylesheets/base";

.task_entry {
	width: 100%;
	background-color: inherit;
	color: inherit;
}

.task {
	width: 100%;
	line-height: 30px;
	font-size: 20px;
	font-family: 'Roboto', sans-serif;
	box-sizing: border-box;
	padding: 5px;
	text-align: justify;
	background-color: inherit;
	color: inherit;
}

.mark_done_button {
	width: 20px;
	height: 20px;
	margin-left: 5px;
	background-color: green;
	display: inline;
}

.delete_button {
	width: 20px;
	height: 20px;
	margin-left: 5px;
	background-color: $warning_red;
	display: inline;
}
</style>
