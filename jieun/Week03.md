# 10814. 나이순 정렬

```python
import sys
input = sys.stdin.readline
n = int(input())
member = []
for _ in range(n):
    a, b = input().split()
    member.append([int(a), b])

mem = sorted(member, key=lambda x: x[0])
for i in range(n):
    print(*mem[i])
```



# 2556. 단지번호 붙이기

```python
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = int(input())
maps = [list(input()) for _ in range(n)]

q = deque()
dan = 0
dan_list = []

for i in range(n):
    for j in range(n):
        if maps[i][j] == '1' :
            q.append((i, j))
            maps[i][j] = 0
            dan += 1
            cnt = 1
            while q:
                y, x = q.pop()

                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if ny >= 0 and ny < n and nx >= 0 and nx < n:
                        if maps[ny][nx] == '1' :
                            q.append((ny, nx))
                            maps[ny][nx] = 0
                            cnt += 1
            dan_list.append(cnt)

dan_list.sort()
print(dan)
for d in dan_list:
    print(d)
```



