// File: frontend/src/stores/championStore.ts
import { defineStore } from 'pinia';
import axios from 'axios';

export const useChampionStore = defineStore('champion', {
  state: () => ({
    champions: [] as Array<any>,
    searchQuery: '',
    selectedRole: ''
  }),
  getters: {
    filteredChampions(state) {
      return state.champions.filter(champ => {
        const matchesName = champ.name.includes(state.searchQuery);
        const matchesRole = state.selectedRole ? champ.tags.includes(state.selectedRole) : true;
        return matchesName && matchesRole;
      });
    }
  },
  actions: {
    async loadChampions() {
      const res = await axios.get('/static-champions');
      this.champions = res.data;
    },
    setSearch(query: string) {
      this.searchQuery = query;
    },
    setRole(role: string) {
      this.selectedRole = this.selectedRole === role ? '' : role;
    }
  }
});
