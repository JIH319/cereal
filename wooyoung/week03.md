# week 03



### 1.나이순 정렬 

### [10814번: 나이순 정렬 (acmicpc.net)](https://www.acmicpc.net/problem/10814)

온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

```python
import sys
input=sys.stdin.readline

N = int(input())
user = []

for _ in range(N):
    user.append(list(input().split()))
print(user)
user.sort(key=lambda a:int(a[0]))
print(user)
for i in range(N):
    print(user[i][0], user[i][1])
```



### 3. 단지번호 붙이기  

## [백준/2556\]단지번호 붙이기](https://www.acmicpc.net/problem/2667)

```python
# 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

def solve(area, sr, sc):
    global cnt
    # 다시 못오게 0으로 만들어 버리기
    area[sr][sc] = '0'
    # 단지 속 아파트 갯수
    cnt += 1

    # 현재 위치에서 탐색방향 우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for q in range(4):
        nr = sr + dr[q]
        nc = sc + dc[q]

        # 단지내에 아파트가 있다! (단지가 있다)
        if 0 <= nr < N and 0 <= nc < N and area[nr][nc] == '1':
            # 새로운 단지 내 아파트에서 재귀함수 호출
            solve(area, nr, nc)


N = int(input())
area = [list(input()) for _ in range(N)]
apt = []

for i in range(N):
    for j in range(N):
        if area[i][j] == '1':
            cnt = 0
            solve(area, i, j)
            apt.append(cnt)

apt.sort()
print(len(apt))
for a in apt:
    print(a)
```

