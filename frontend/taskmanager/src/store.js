import { createStore } from "vuex";

export const store = createStore({
	state () {
		return {
			fetch_lists: 0,
			selected_list: {
				id: 0,
				name: ""
			}
		}
	},
	mutations: {	
		trigger_fetch_lists (state) {
			state.fetch_lists = 1
		},
		stop_fetch_lists (state) {
			state.fetch_lists = 0
		},
		select_list (state, selected_list_object) {
			state.selected_list = selected_list_object
		}
	}
});
