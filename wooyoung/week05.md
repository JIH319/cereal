# 유기농배추

```python
import sys
input = sys.stdin.readline

def solve(farm,r,c):
    global cnt

    farm[r][c] = 0
    cnt += 1
    # 현재 위치에서 탐색방향 우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for q in range(4):
        nr = r + dr[q]
        nc = c + dc[q]

        # 근처에 벌레 있다!
        if 0 <= nr < M and 0 <= nc < N and farm[nr][nc] == 1:
            solve(farm,nr, nc)

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split()) # 가로, 세로, 배추갯수
    farm = [[0] * N for _ in range(M)]
    for _ in range(K):
        i, j = map(int,input().split())
        farm[i][j] = 1

    bugs = []
    for i in range(M):
        for j in range(N):
            if farm[i][j] == 1:
                cnt = 0
                solve(farm, i,j)
                bugs.append(cnt)
    print(len(bugs))
```



# 연월일달력

```python
T = int(input())
for tc in range(1, T+1):
    N = input()
    year = N[:4]
    month = N[4:6]
    day = N[6:]

    result = 1
    while True:
        if not ('01' <= month <= '12'):
            result = -1
            break

        if month in ('01', '03', '05', '07', '08', '10', '12'):
            if not ('01' <= day <= '31'):
                result = -1
                break

        if month in ('04', '06', '09', '11'):
            if not ('01' <= day <= '30'):
                result = -1
                break

        if month == '02':
            if not ('01' <= day <= '28'):
                result = -1
                break

        break

    if result == 1:
        print(f'#{tc} {year}/{month}/{day}')
    else:
        print(f'#{tc} {result}')
```

