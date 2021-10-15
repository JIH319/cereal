# 17070. 파이프 옮기기 1
import sys
input = sys.stdin.readline


def dfs(y, x, d):
    global cnt
    if y == N - 1 and x == N - 1:
        cnt += 1
        return

    if d == 0:
        if x+1<N and not house[y][x+1]:
            dfs(y,x+1,0)
        if x+1<N and y+1<N and not house[y+1][x] and not house[y+1][x+1] and not house[y][x+1]:
            dfs(y+1,x+1,1)
    elif d == 1:
        if x+1<N and not house[y][x+1]:
            dfs(y,x+1,0)
        if x+1<N and y+1<N and not house[y+1][x] and not house[y+1][x+1] and not house[y][x+1]:
            dfs(y+1,x+1,1)
        if y+1<N and not house[y+1][x]:
            dfs(y+1,x,2)
    elif d == 2:
        if x + 1 < N and y + 1 < N and not house[y + 1][x] and not house[y + 1][x + 1] and not house[y][x + 1]:
            dfs(y + 1, x + 1, 1)
        if y + 1 < N and not house[y + 1][x]:
            dfs(y + 1, x, 2)


# [ 입력 ]
N = int(input())  # 첫째 쭐에 집의 크기가 주어진다.
house = [list(map(int, input().split()))[:N] for _ in range(N)]
# 현재 위치에 따라 dfs 를 해주자. 0은 0도, 1은 45도, 2는 90도로 하자.
cnt = 0
dfs(0, 1, 0)
print(cnt)
