### [백준/2003] 수들의 합2

```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 리스트에 nums 첫번째 요소를 저장함
sum_lst = [nums[0]]
# 0부터 i 번째까지의 누적 합계를 sum_lst에 저장
for i in range(N-1):
    sum_lst.append(sum_lst[i]+nums[i+1])

cnt = 0
# 수열을 더해서 M이 될 수 있는 것을 찾음
for j in range(N-1, -1, -1):
    if sum_lst[j] > M:
        for i in range(j-1, -1, -1):
            num_sum = sum_lst[j] - sum_lst[i]
            if num_sum == M:
                cnt += 1
                break
            elif num_sum > N:
                break
    elif sum_lst[j] == M:
        cnt += 1

print(cnt)
```

```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

s, e = 0, 0
num_sum, cnt = 0, 0
for s in range(N):
    while num_sum < M and e < N:
        num_sum += nums[e]
        e += 1
    if num_sum == M:
        cnt += 1
    num_sum -= nums[s]

print(cnt)
```



### [SWEA/1949] 등산로 조성

```python
def dfs(r, c, chance):
    global MAX, visited
    MAX = max(MAX, visited[r][c])
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = r + dr
        nc = c + dc
        if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
            continue
        if arr[r][c] > arr[nr][nc]:
            visited[nr][nc] = visited[r][c] + 1
            dfs(nr, nc, chance)
            visited[nr][nc] = 0
        elif chance and arr[nr][nc] - K < arr[r][c]:
            temp = arr[nr][nc]
            arr[nr][nc] = arr[r][c] - 1
            visited[nr][nc] = visited[r][c] + 1
            dfs(nr, nc, chance-1)
            visited[nr][nc] = 0
            arr[nr][nc] = temp


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = []
    top = 0
    for i in range(N):
        arr.append(list(map(int, input().split())))
        for j in range(N):
            if arr[i][j] > top:
                top = arr[i][j]
    MAX = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == top:
                visited[i][j] = 1
                dfs(i, j, 1)
                visited[i][j] = 0

    print("#{} {}".format(tc, MAX))
```



