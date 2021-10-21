### [백준/1213] 팰린드롬 만들기

```python
import sys

input = sys.stdin.readline
lst = list(input().strip())
dic = {}

for k in lst:
    if k in dic.keys():
        dic[k] += 1
    else:
        dic[k] = 1

odd, even = 0, 0
for v in dic.values():
    if v%2:
        odd += 1
    else:
        even += 1

# 1. 홀수 개인 문자가 없고 짝수 개인 문자만 있는 경우
# 2. 홀수 개인 문자가 1개 있고 짝수 개인 문자가 있는 경우
# 3. 홀수 한개인 문자만 있는 경우
if odd > 1:	# 홀수가 2개이상이면 회문 만들 수 없음
    print("I'm Sorry Hansoo")
else:
    keys = list(dic.keys())
    keys.sort()
    length = len(lst)  # 문자열 길이
    pal = [''] * length
    i, temp = 0, 0
    for k in keys:
        if dic[k] > 1:
            if dic[k] % 2:
                temp = k
            for j in range(dic[k] // 2):
                pal[0 + i] = k
                pal[length - 1 - i] = k
                i += 1
        else:  # 홀수 개 문자
            temp = k
    if temp:  # temp이 0이 아니면
        pal.insert(length // 2, temp)
    for ans in pal:
        print(ans, end='')
```



### [백준/17070] 파이프 옮기기 1

```python
import sys
input = sys.stdin.readline


def dfs(cur, dir):
    global cnt
    ci, cj = cur
    if ci == N - 1 and cj == N - 1:
        cnt += 1
        return
    if 0 <= ci+1 < N and 0 <= cj+1 < N and not arr[ci+1][cj] and not arr[ci][cj+1] and not arr[ci+1][cj+1]:
        dfs((ci+1, cj+1), 2)
    if dir == 0 or dir == 2: # 가로 또는 대각선
        if 0 <= cj+1 < N and not arr[ci][cj+1]:
            dfs((ci, cj+1), 0)
    if dir == 1 or dir == 2: # 세로 또는 대각선
        if 0 <= ci+1 < N and not arr[ci+1][cj]:
            dfs((ci+1, cj), 1)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dfs((0, 1), 0)
print(cnt)

```



```python
import sys
input = sys.stdin.readline


# 파이프의 뒤쪽은 앞쪽이 이동하면 그 자리로 오기 때문에
# 앞쪽 파이프만 이동가능한지 조사
# 파이프가 (N-1, N-1)으로 갈 수 있는 경우의 수를 구하기
def dfs(pre, cur): # cur: 파이프의 앞쪽(나아가는 쪽)의 행과 열
    global cnt
    pi, pj = pre
    ci, cj = cur
    if ci == N - 1 and cj == N - 1:
        cnt += 1
        return
    # 지금 파이프가 가론지 세론지 대각선인지 알아야 함
    if pi == ci:
        d = [(0, 1), (1, 1)] # 가로
    elif pj == cj:
        d = [(1, 0), (1, 1)] # 세로
    else:
        d = [(0, 1), (1, 0), (1, 1)] # 대각선
    for di, dj in d:
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N and not arr[ni][nj]:
            if di == 1 and dj == 1: # 대각선으로 움직인다면 3방향 확인
                if not arr[ci+1][cj] and not arr[ci][cj+1]:
                    dfs(cur, (ni, nj))
            else:   # 대각선으로 움직이는게 아니라면
                dfs(cur, (ni, nj))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dfs((0, 0), (0, 1))
print(cnt)

```

