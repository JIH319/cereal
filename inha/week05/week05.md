### [백준/1012] 유기농 배추

```python
import sys

input = sys.stdin.readline


# dfs 이용
def dfs(s, e):
    global cnt
    adj[s][e] = 0
    stack = [(s,e)]
    while stack:
        c = stack[-1]
        ci, cj = c[0], c[1]
        # 상하좌우로 옮겨갈 수 있는 배추가 있는지 확인
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < N and 0 <= nj < M and adj[ni][nj]:
                adj[ni][nj] = 0 # 이미 방문한 배추는 0이로 인접행렬에 표시해줌
                stack.append((ni, nj))
                break
        else: # 상하좌우로 더이상 연결된 배추가 없음
            stack.pop()
    cnt += 1


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    adj = [[0]*M for _ in range(N)] # N X M 의 인접행렬 만듦
    # input을 받아서 인접행렬에 배추가 있는 곳을 표시해줌
    for _ in range(K):
        j, i = map(int, input().split())
        adj[i][j] = 1
    cnt = 0
    i = 0
    while i < N:
        j = 0
        while j < M:
            # 인접행렬에서 1인 곳(배추가 있는 곳)을 찾음
            if adj[i][j] == 1:
                s, e = i, j
                dfs(i, j)
            j += 1
        i += 1
    print(cnt)
```



### [SWEA/2056] 연월일 달력

```python
def check(month, day):
    # 유효한 월, 일인지 확인
    # 문자열을 정수타입으로 변환
    month = int(month)
    day = int(day)
    result = False
    # 경우를 나눠서 비교
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= day <= 31:
            result = True
    elif month in [4, 6, 9, 11]:
        if 1 <= day <= 30:
            result = True
    elif month == 2:
        if 1 <= day <= 28:
            result = True
    # 유효하면 result는 True, 유효하지 않으면 result는 False 반환
    return result


T = int(input())

for tc in range(1, T+1):
    nums = input() # 문자열로 그대로 받아옴
    # 년, 월, 일 슬라이싱으로 자름
    y = nums[0:4]
    m = nums[4:6]
    d = nums[6:8]

    if check(m, d): # 유효한 연월일이면
        print('#{} {}/{}/{}'.format(tc, y, m, d))
    else:
        print('#{} {}'.format(tc, -1))
```



### [백준/5639] 나무 재테크

```python

```

