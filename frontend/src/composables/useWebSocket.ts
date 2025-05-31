// File: frontend/src/composables/useWebSocket.ts
import { ref, onBeforeUnmount } from 'vue';

export function useWebSocket(matchId: number, gameNo: number) {
  // 백엔드 WebSocket URL에 맞춰 수정하세요
  const url = `ws://localhost:8000/ws/match/${matchId}/game/${gameNo}`;
  const socket = new WebSocket(url);
  const messages = ref<Array<any>>([]);

  socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    messages.value.push(data);
  };

  socket.onerror = (err) => {
    console.error('WebSocket error:', err);
  };

  // 컴포넌트 언마운트 시 소켓 종료
  onBeforeUnmount(() => {
    socket.close();
  });

  // 서버로 메시지 전송 함수
  function send(payload: any) {
    socket.send(JSON.stringify(payload));
  }

  return { messages, send };
}
