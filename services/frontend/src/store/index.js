import createPersistedState from "vuex-persistedstate";
import { createStore } from 'vuex';

import notes from './modules/notes';
import users from './modules/users';


const store = createStore({
  modules: {
    notes,
    users,
  },
  plugins: [createPersistedState()]
});

export default store;