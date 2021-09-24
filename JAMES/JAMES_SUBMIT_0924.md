# 나이순 정렬

```python
import sys
input = sys.stdin.readline

N = int(input())
data = [input().split() for _ in range(N)]
data.sort(key= lambda x : int(x[0]))  #첫번째 꺼만 정수형으로 바꿔줘서 솔트해준다.. 
#람다로 솔트하는법은 그때 프로젝트때인가 한거 같아스 ㅎㅎㅎ 람다 구글링해봄..
for i in data:
    print(*i)
```

# 삼성이의 트라우마 극복

```python
문제 보기만 해도 하기싫어지는 문제......
```

# 단지번호붙이기

```python
import sys
input = sys.stdin.readline

from collections import deque


def bfs(r, c): #전에 수업때 진행한 코드 줍줍 ㅎㅎ
    queue = deque()
    queue.append((r, c))
    visited[r][c] = 1
    cnt = 0 # 각 단지들의 합을 구해기 위한 초기화

    while queue:
        cr, cc = queue.popleft()
        cnt += 1 #한개를 할때마다 1++

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = cr + dr, cc + dc

            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                queue.append((nr, nc))
                visited[nr][nc] = 1

    return cnt #한개 단지동안 모은거


N = int(input())
arr = [list(map(int, input())) for _ in range(N)] #데이터 받아주구
visited = [[0] * N for _ in range(N)] #방문기록 남길곳 만들어 주구
results = [] #각 구간의 합 넣을곳 만들어주구
rst = 0 #구간의 개수 초기화
for i in range(N): #1인 곳 찾기
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]: #1이면서 방문안한곳부터 시작
            results.append(bfs(i, j)) #한번 구간을 다 돌면 bfs를 통해 각 구간의 합을 모아서 가져온다
            rst += 1 # 그러면 한 구간 finish

print(rst)
results.sort()
for result in results:
    print(result)
```

