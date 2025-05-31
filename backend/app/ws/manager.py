# backend/app/ws/manager.py

from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from app.db.session import get_db
from app.crud.banpick import create_banpick
from sqlalchemy.ext.asyncio import AsyncSession
from app.banpick_logic import GameManager

router = APIRouter()
# 매치별로 GameManager 인스턴스를 관리 (간단 예시)
game_managers: dict[int, GameManager] = {}

@router.websocket("/ws/match/{match_id}/game/{game_no}")
async def websocket_endpoint(
    websocket: WebSocket,
    match_id: int,
    game_no: int,
    db: AsyncSession = Depends(get_db),
):
    await websocket.accept()
    # 매치·게임별 매니저 준비
    key = (match_id, game_no)
    if key not in game_managers:
        game_managers[key] = GameManager()
    mgr = game_managers[key]

    try:
        while True:
            data = await websocket.receive_json()
            team = data["team"]            # "blue" 또는 "red"
            action = data["action"]        # "BAN" 또는 "PICK"
            champ_id = data["champion_id"] # 챔피언 테이블 PK

            try:
                record = mgr.perform(team, action, champ_id)
            except ValueError as e:
                # 잘못된 순서 등 오류 응답
                await websocket.send_json({"type": "error", "message": str(e)})
                continue

            # DB에 저장
            db_rec = await create_banpick(
                db,
                {
                    "match_id": match_id,
                    "team_id": 1 if team=="blue" else 2,   # 팀 매핑 로직 예시
                    "order_index": record["order"],
                    "action_type": action,
                    "champion_id": champ_id
                }
            )
            # 모든 클라이언트에 업데이트 브로드캐스트 (간단 예시)
            await websocket.send_json({"type": "update", "record": record})

    except WebSocketDisconnect:
        # 연결 종료 처리
        pass
