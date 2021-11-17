# 1783. 병든 나이트
import sys
from collections import deque
input = sys.stdin.readline

def dfs(y,x):
    chess[y][x]=1
    for i in range(4):
        ny, nx = y+dy[i],x+dx[i]
        if 0<=ny<N and 0<=nx<M:
            dfs(ny,nx)


dy = [-2,-1,1,2]
dx = [1,2,2,1]
N, M = map(int,input().split()) # 세로길이, 가로길이

chess = [[0]*M for _ in range(N)]
dfs(N-1,0)
result = 0
for i in range(N):
    result += sum(chess[i])
print(chess)
print(result)

