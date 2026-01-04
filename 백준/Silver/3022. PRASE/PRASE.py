import sys

def solve():
    # N 입력 (음식을 가져간 횟수)
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
    except ValueError:
        return

    eaten_count = {}  # 아이별로 먹은 음식 개수를 저장하는 딕셔너리
    total_eaten = 0   # 지금까지 소비된 전체 음식의 개수
    warnings = 0      # 경고 횟수 카운트

    for _ in range(n):
        name = sys.stdin.readline().strip()
        
        # 1. 이 아이가 이전에 먹은 양을 가져옴 (처음이면 0)
        current_child_eaten = eaten_count.get(name, 0)
        
        # 2. 나머지 아이들이 먹은 총합 계산
        # 나머지 = 전체 먹은 양 - 이 아이가 먹은 양
        others_eaten = total_eaten - current_child_eaten
        
        # 3. 조건 확인: 이 아이가 이미 먹은 양 > 나머지 아이들이 먹은 양 합계
        if current_child_eaten > others_eaten:
            warnings += 1
            
        # 4. 데이터 업데이트 (방금 먹은 조각 추가)
        eaten_count[name] = current_child_eaten + 1
        total_eaten += 1

    # 결과 출력
    print(warnings)

if __name__ == "__main__":
    solve()