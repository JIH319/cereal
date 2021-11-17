# 16198. 에너지 모으기
import sys

input = sys.stdin.readline


# 해결하기 위한 solve 함수
def solve(val):
    global result
    M = len(marble)
    # marble 이 2개만 남아을 경우, 그 값이 저장 값보다 큰지 비교후 대입
    if M == 2:
        if val > result:
            result = val
    # 첫번째 구슬과 마지막 구슬은 선택할 수 없으므로,
    for i in range(1, M - 1):
        # 에너지는 더해주고, 구슬은 날려준다.
        sum_m = marble[i - 1] * marble[i + 1]
        tmp = marble.pop(i)
        solve(val + sum_m)
        # 날린 구슬을 닷시 넣어준다 (브루트-포스)
        marble.insert(i, tmp)


# [ 입 력 ]
N = int(input())  # 구슬의 갯수
marble = list(map(int, input().split()))[:N]
result = 0
solve(0)
print(result)
