# backend/app/banpick_logic.py

def generate_draft_sequence():
    """
    프로 경기 토너먼트 드래프트 순서:
    1) Ban Phase 1: Blue 3회, Red 3회 (교대로)
    2) Pick Phase 1: Blue(1), Red(2), Blue(2), Red(1)
    3) Ban Phase 2: Red 2회, Blue 2회 (교대로)
    4) Pick Phase 2: Red(1), Blue(2), Red(1)
    """
    seq = []

    # Ban Phase 1 (총 6회)
    for _ in range(3):
        seq.append({"action": "BAN", "team": "blue"})
        seq.append({"action": "BAN", "team": "red"})

    # Pick Phase 1 (총 6회)
    seq.append({"action": "PICK", "team": "blue"})
    seq.extend([{"action": "PICK", "team": "red"}] * 2)
    seq.extend([{"action": "PICK", "team": "blue"}] * 2)
    seq.append({"action": "PICK", "team": "red"})

    # Ban Phase 2 (총 4회)
    for _ in range(2):
        seq.append({"action": "BAN", "team": "red"})
        seq.append({"action": "BAN", "team": "blue"})

    # Pick Phase 2 (총 4회)
    seq.append({"action": "PICK", "team": "red"})
    seq.extend([{"action": "PICK", "team": "blue"}] * 2)
    seq.append({"action": "PICK", "team": "red"})

    return seq
# backend/app/banpick_logic.py (계속)

class GameManager:
    def __init__(self):
        self.sequence = generate_draft_sequence()
        self.current = 0
        self.records = []  # 수행된 밴픽 기록

    def next_step(self):
        """다음 순서를 반환하거나, 없으면 None."""
        if self.current < len(self.sequence):
            return self.sequence[self.current]
        return None

    def perform(self, team: str, action: str, champion_id: int):
        """요청된 밴픽이 올바르면 기록하고, 다음으로 진행."""
        expected = self.next_step()
        if not expected:
            raise ValueError("밴픽 단계가 모두 완료되었습니다.")
        if expected["team"] != team or expected["action"] != action:
            raise ValueError(f"잘못된 순서입니다. 기대: {expected}")
        # 올바른 요청이면 기록
        record = {"order": self.current + 1, "team": team, "action": action, "champion_id": champion_id}
        self.records.append(record)
        self.current += 1
        return record
