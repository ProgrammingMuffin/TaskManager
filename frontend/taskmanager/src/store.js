import { createStore } from "vuex";

export const store = createStore({
	state () {
		return {
			fetch_lists: 0
		}
	},
	mutations: {	
		trigger_fetch_lists (state) {
			state.fetch_lists = 1
		},
		stop_fetch_lists (state) {
			state.fetch_lists = 0
		}
	}
});
