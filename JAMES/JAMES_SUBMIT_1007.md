# 연월일달력

```python
#책에서 오늘 진도나간 range를 사용하고자 했당 ㅎㅎㅎ 레인지가 제너레이터중에서 메모리를 젤 적게 먹는다고 했는데 결과적인 메모리는 비슷한거 같다..[:]요고 때문인가... 메모리, 코드길이 겁나 작게 만들고싶다... 공통적인 부분 묶어서 하고싶은데 재테크때문에 머리가 멈췄다

for tc in range(1, 1+int(input())):
    YMD = list(input())
    month = range(1, 13) # 월
    a = range(1,32) # 나머지
    b = range(1,31) # 30일까지
    c = range(1,29) # 2월만
    d = [4, 6, 9, 11] #30일을 가진 월

    print('#{}'.format(tc), end=' ')

    #일단 달이면
    if int(''.join(YMD[4:6])) in month:
    #2월이면
        if int(''.join(YMD[4:6])) == 2:
            if int(''.join(YMD[6:8])) in c:
                print(''.join(YMD[:4]),end='/')
                print(''.join(YMD[4:6]), end='/')
                print(''.join(YMD[6:8]))
            else:
                print(-1)


    #30일까지인 달이면
        elif int(''.join(YMD[4:6])) in d:
            if int(''.join(YMD[6:8])) in b:
                print(''.join(YMD[:4]),end='/')
                print(''.join(YMD[4:6]), end='/')
                print(''.join(YMD[6:8]))
            else:
                print(-1)

    #나머지
        else:
            if int(''.join(YMD[6:8])) in a:
                print(''.join(YMD[:4]),end='/')
                print(''.join(YMD[4:6]), end='/')
                print(''.join(YMD[6:8]))
            else:
                print(-1)

    else:
        print(-1)
```

# 유기농배추춫

```python
import sys
input = sys.stdin.readline

from collections import deque


def dfs(r, c): #친숙 ㅎㅎㅎ 우영 멋찜!
    queue = deque()
    queue.append((r, c))
    arr[r][c] = 0

    while queue:
        cr, cc = queue.popleft()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = cr + dr, cc + dc

            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
                queue.append((nr, nc))
                arr[nr][nc] = 0

    return


for _ in range(int(input())):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    cnt = 0

    for _ in range(K): #배추 넣어주공!
        c, r = map(int, input().split())
        arr[r][c] = 1

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1: #1인 좌표부터 시이작
                dfs(r, c)
                cnt += 1 # 그 구역 끝나믄 벌레였나? 그거 하나 증가 

    print(cnt)

```

# 나무 재테크 - 미틴놈임...

```python

# 가장 처음에 양분은 모든 칸에 5만큼 들어있다. -> 시작부터 5를 넣고 리스트를 만들어야겠군
# 봄에는 나무가 자신의 나이만큼 양분을 먹고,
# 나이가 1 증가한다.하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
# 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
# 여름에는 봄에 죽은 나무가 양분으로 변하게 된다. 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점 아래는 버린다.
# 가을에는 나무가 번식한다. 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
# 어떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다.
# 겨울에는 땅에 양분을 추가한다. 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.
# K년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하는 프로그램을 작성하시오.
    
```

# 
