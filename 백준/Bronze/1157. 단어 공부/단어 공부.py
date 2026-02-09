word = input().upper()
alpha = [0] * 26

# 1. 알파벳 빈도수 계산 (이 부분은 원래 코드와 동일하며 아주 좋습니다)
for char in word:
    index = ord(char) - ord('A')
    alpha[index] += 1

# 2. 최대 빈도수 찾기
max_freq = max(alpha)

# 3. 최대 빈도수를 가진 알파벳이 몇 개인지 확인
# 만약 alpha 리스트에서 max_freq의 개수가 2개 이상이면 ? 출력
if alpha.count(max_freq) > 1:
    print("?")
else:
    # 아니라면, max_freq 값을 가진 인덱스를 찾아서 알파벳으로 변환해 출력
    # alpha.index(max_freq)는 리스트에서 해당 값의 첫 번째 인덱스를 반환
    max_index = alpha.index(max_freq)
    print(chr(max_index + ord('A')))