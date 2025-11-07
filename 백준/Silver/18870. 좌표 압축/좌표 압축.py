import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
unique_arr = set(arr) # 중복을 없애준다.
sorted_arr = sorted(unique_arr)
dict_arr = {sorted_arr[i]: i for i in range(len(sorted_arr))}
#2 4 -10 4 -9를 입력 받으면, {-10: 0, -9: 1 ...} 이런식으로 되는거임
result = [dict_arr[i] for i in arr] 
#그러고 원래 값을 인덱스로 사용해서 해당 숫자를 출력 arr이 4 라면 dirt_arr[4]는 3이니까, arr 원소 4위치에 다 3이 들어가는 것.

print(*result)