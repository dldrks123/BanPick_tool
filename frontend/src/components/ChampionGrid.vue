<!-- File: frontend/src/components/ChampionGrid.vue -->
<template>
  <div>
    <input
      v-model="search"
      placeholder="챔피언 이름 검색"
      class="border p-2 mb-4 w-full"
    />

    <div class="flex space-x-2 mb-4">
      <button
        v-for="role in roles"
        :key="role"
        @click="toggleRole(role)"
        :class="[
          'px-3 py-1 rounded',
          { 'bg-blue-500 text-white': selectedRole === role }
        ]"
      >
        {{ role }}
      </button>
    </div>

    <div class="grid grid-cols-6 gap-4">
      <div
        v-for="champ in filteredChampions"
        :key="champ.id"
        class="cursor-pointer"
        @click="onSelect(champ)"
      >
        <img
          :src="`https://ddragon.leagueoflegends.com/cdn/13.14.1/img/champion/${champ.image}`"
          :alt="champ.name"
          class="w-full rounded-lg shadow"
        />
        <div class="text-center mt-2">
          {{ champ.name }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue';
import { useChampionStore } from '../stores/championStore';

// defineEmits를 함수 시그니처 형태로 정의
const emit = defineEmits<{
  (event: 'select', champ: any): void;
}>();

const championStore = useChampionStore();
const roles = ['Top', 'Jungle', 'Mid', 'ADCarry', 'Support'];

const search = ref('');
onMounted(() => {
  championStore.loadChampions();
});

watch(search, (val) => championStore.setSearch(val));

function toggleRole(role: string) {
  championStore.setRole(role);
}

function onSelect(champ: any) {
  emit('select', champ);
}

const filteredChampions = computed(() => championStore.filteredChampions);
const selectedRole = computed(() => championStore.selectedRole);
</script>

<style scoped>
/* 필요에 따라 추가 스타일링 */
</style>
