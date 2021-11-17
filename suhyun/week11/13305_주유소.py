# 13305. 주유소
import sys

input = sys.stdin.readline

N = int(input())  # 도시의 개수
road = list(map(int, input().split()))[:N - 1]
oil = list(map(int, input().split()))[:N]
s = 0  # 현재 위치
rst = 0
# 현재위치가 아직 주유소 끝을 도달하지 않았을 때,
while s <= N:
    c = s
    # 다음 정류소부터 마지막 전 정류소까지 반복문을 돌린다.
    for i in range(s + 1, N - 1):
        # 현재 정류소보다 더 값싼 정류소를 찾을 경우, 그 위치를 저장하고 break
        if oil[s] > oil[i]:
            c = i
            break
    # 마지막 전 정류소까지 가격이 동일할 경우 이다. 이 경우 위치를 N-1 로 저장하고 나간다.
    else:
        c = N - 1
    # 시작 위치부터 현재위치까지 기름 값을 rst t에 더해준다.
    # for j in range(s, c):
    #     rst += oil[s] * road[j]
    rst += oil[s]*sum(road[s:c])
    s = c
    # 만약, 시작위치에서 +1 한 값이 정류소 보다 클경우, 해당 oil 값은 다 구했으므로 while 문을 나간다.
    if s + 1 >= N:
        break
print(rst)
