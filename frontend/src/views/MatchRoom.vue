<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Match {{ matchId }} — Game {{ gameNo }}</h1>

    <!-- 1) Champion 선택 그리드 -->
    <ChampionGrid @select="onChampionSelect" />

    <!-- 2) Ban / Pick 패널 -->
    <div class="mt-6 grid grid-cols-2 gap-4">
      <div>
        <h2 class="text-xl mb-2 text-red-600">Red Team</h2>
        <ul>
          <li v-for="rec in redHistory" :key="rec.order">
            {{ rec.order }}. {{ rec.action }} {{ rec.champion_name }}
          </li>
        </ul>
      </div>
      <div>
        <h2 class="text-xl mb-2 text-blue-600">Blue Team</h2>
        <ul>
          <li v-for="rec in blueHistory" :key="rec.order">
            {{ rec.order }}. {{ rec.action }} {{ rec.champion_name }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { useRoute } from 'vue-router';
import ChampionGrid from '@/components/ChampionGrid.vue';
import { useWebSocket } from '@/composables/useWebSocket';

// URL 파라미터에서 matchId, gameNo 가져오기
const route = useRoute();
const matchId = Number(route.params.matchId ?? 1);
const gameNo  = Number(route.params.gameNo  ?? 1);

// WebSocket 훅 사용
const { messages, send } = useWebSocket(matchId, gameNo);

// onChampionSelect 호출 시 WS로 메시지 전송
function onChampionSelect(champ: any) {
  // 예: 교대로 blue/red, BAN/PICK 로직은 백엔드 GameManager가 검증
  send({
    team: 'blue',           // 실제론 화면 버튼이나 상태에 따라 'blue' 또는 'red'
    action: 'PICK',         // 'BAN' 또는 'PICK'
    champion_id: champ.id
  });
}

// 받은 메시지를 팀별/액션별로 나누어 보여주기
const blueHistory = computed(() =>
  messages.value
    .filter(m => m.type === 'update' && m.record.team === 'blue')
    .map(m => ({
      order: m.record.order,
      action: m.record.action,
      champion_name: m.record.champion_name ?? m.record.champion_id
    }))
);

const redHistory = computed(() =>
  messages.value
    .filter(m => m.type === 'update' && m.record.team === 'red')
    .map(m => ({
      order: m.record.order,
      action: m.record.action,
      champion_name: m.record.champion_name ?? m.record.champion_id
    }))
);
</script>

<style scoped>
/* 필요시 스타일 조정 */
</style>
