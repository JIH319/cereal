#### 6603. 로또

```python
# 6603 로또
import sys
from collections import deque

input = sys.stdin.readline


# 맞은거. dfs 로하자 s 는 시작지점, d는 길이
def dfs(s, d):
    # 길이가 6에 도달하면, 출력해주자
    if d == 6:
        print(*comb[:6])
        return
    # 반복문을 돌면서, 아직 확인안한 값들을 dfs 로 넘가주자
    for i in range(s, len(arr)):
        comb[d] = arr[i]
        dfs(i + 1, d + 1)


# 0 이 나올때까지 반복해야하므로, 반복문을 True 로 해주자.
while True:
    # 배열을 가져오되, 맨 왼쪽값을 날려버리자.
    arr = deque(list(map(int, input().split())))
    arr.popleft()
    # 그 깅ㄹ이에 맞게끔 조합 배열을 만들어주자.
    n = len(arr)
    comb = [0 for i in range(n)]
    # 길이가 0이면, 종료하자
    if not n:
        break
    # 시작지점 0, 길이 0부터 dfs 로 돌려주자.
    dfs(0, 0)
    print()
# 틀린거
#     result = []
#     for i in range(1 << n):
#         rst = []
#         for j in range(n):
#             if i & (1 << j):
#                 rst.append(arr[j])
#         # if len(rst)==6 and not rst in result:
#         if len(rst) == 6:
#             print(*rst)
#     print('')


```



#### 11399. ATM

```python
# 11399. ATM
# 인하은행
N = int(input())  # 사람의 수
arr = list(map(int, input().split()))[:N]
# 최소 값은 오름차순 배열일 때 가능하다.
arr.sort()
# 최종 합
result = 0
# 더해지는 시간
money_time = 0
for i in range(N):
    money_time += arr[i]
    result += money_time
print(result)


```



#### 16198. 에너지 모으기

```python
# 16198. 에너지 모으기
import sys

input = sys.stdin.readline


# 해결하기 위한 solve 함수
def solve(val):
    global result
    M = len(marble)
    # marble 이 2개만 남아을 경우, 그 값이 저장 값보다 큰지 비교후 대입
    if M == 2:
        if val > result:
            result = val
    # 첫번째 구슬과 마지막 구슬은 선택할 수 없으므로,
    for i in range(1, M - 1):
        # 에너지는 더해주고, 구슬은 날려준다.
        sum_m = marble[i - 1] * marble[i + 1]
        tmp = marble.pop(i)
        solve(val + sum_m)
        # 날린 구슬을 닷시 넣어준다 (브루트-포스)
        marble.insert(i, tmp)


# [ 입 력 ]
N = int(input())  # 구슬의 갯수
marble = list(map(int, input().split()))[:N]
result = 0
solve(0)
print(result)

```



#### 13305. 주유소

```python
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
    for j in range(s, c):
        rst += oil[s] * road[j]
    s = c
    # 만약, 시작위치에서 +1 한 값이 정류소 보다 클경우, 해당 oil 값은 다 구했으므로 while 문을 나간다.
    if s + 1 >= N:
        break
print(rst)

```



#### 1931. 회의실 배정

```python
# 1931. 회의실 배정
import sys

input = sys.stdin.readline

N = int(input())  # 회의의 수
arr = [[0] * 2 for _ in range(N)]  # 회의 시간
for i in range(N):
    arr[i][0], arr[i][1] = map(int, input().split())  # 각 요소를 일단 대입해주자.

arr.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간 , 시작 시간 오름차순으로 정렬

cnt = 1  # 첫 회의는 무조건 하니까 1부터 시작
end = arr[0][1]  # 첫 회의가 끝나는 시간.
for i in range(1, N):  # 총 회의 갯수 만큼 반복문
    # 다음 회의 시작시간이 끝시간 보다 크거나 같을경우,
    if arr[i][0] >= end:
        # 그 회의의 끝시간을 대입해주고, cnt+=1 을 해준다.
        end = arr[i][1]
        cnt += 1
print(cnt)


```



#### 1783. 병든 나이트

```python
# 1783. 병든 나이트
# 못품
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



```



#### 18222. 투에 모스 문자열

```python
# 18222. 투에 모스 문자열

# 0 1 2 3 4 5 6 7
# 0 1 1 0 1 0 0 1 

# t0 = 0 
# t1 = 1
# t2n = 1
# t2n+1 = 1-tn
def solve(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 : # 2n+1 을 뜻함
        return 1- solve(n//2)
    else: # 2n 을 뜻함
        return solve(n//2)

# [ 입력 ]
k = int(input())
print(solve(k-1))

```

