##  1213. 팰린드롬 

```python
# 1213_팰린드롬
palindrome = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0,
    'E': 0, 'F': 0, 'G': 0, 'H': 0,
    'I': 0, 'J': 0, 'K': 0, 'L': 0,
    'M': 0, 'N': 0, 'O': 0, 'P': 0,
    'Q': 0, 'R': 0, 'S': 0, 'T': 0,
    'U': 0, 'V': 0, 'W': 0, 'X': 0,
    'Y': 0, 'Z': 0,
}


def verification():
    rst = ''
    cnt = 0
    mid = ''
    for k, v in palindrome.items():
        if v == 0:
            continue
        if v % 2 == 0:
            rst += k * (v // 2)
        elif v % 2 and not cnt:
            rst += k * (v // 2)
            mid = k
            cnt = 1
        elif v % 2 and cnt:
            return 'I\'m Sorry Hansoo'
    return rst + mid + rst[::-1]


N = input()
for i in range(len(N)):
    palindrome[N[i]] += 1
result = verification()
print(result)

```



###  10761. 신뢰

```python
# 10761. 신뢰
def search():
    # bi는 blue 의 현재 위치, oi 는 orange 의 현재 위치
    bi = oi = 0
    rst = 0
    while len(blue) != 0 or len(orange) != 0:
        # 처음 오더가 blue 일 때,
        if robots[0] == 'B':
            if int(robots[1]) - 1 > bi:
                bi += 1
            elif int(robots[1]) - 1 < bi:
                bi -= 1
            # bi 가 일치할 경우, robots 와 blue 의 위치 값을 모두 제거해주자.
            else:
                robots.pop(0)
                robots.pop(0)
                blue.pop(0)

            # orange 도 눌러야될게 있을 경우,
            if len(orange) != 0:
                if oi < orange[0] - 1:
                    oi += 1
                elif oi > orange[0] - 1:
                    oi -= 1
        else:
            if int(robots[1]) - 1 > oi:
                oi += 1
            elif int(robots[1]) - 1 < oi:
                oi -= 1
            # oi 가 일치할 경우, robots 와 orange 의 위치 값을 모두 제거해주자.
            else:
                robots.pop(0)
                robots.pop(0)
                orange.pop(0)

            # blue 도 아직 남아있을 경우,
            if len(blue) != 0:
                if bi < blue[0] - 1:
                    bi += 1
                elif bi > blue[0] - 1:
                    bi -= 1
        rst += 1
    return rst


T = int(input())  # 테스트 케이스의 수 T
for tc in range(1, T + 1):
    robots = list(map(str, input().split()))
    N = int(robots.pop(0))
    blue = []
    orange = []
    for p in range(0, len(robots) - 1, 2):
        if robots[p] == 'B':
            blue.append(int(robots[p + 1]))
        else:
            orange.append(int(robots[p + 1]))
    result = search()
    print('#{} {}'.format(tc, result))

```



### 17070. 파이프 옮기기 1

```python
# 17070. 파이프 옮기기 1
import sys

input = sys.stdin.readline


def dfs(y, x, d):
    global cnt
    if y == N - 1 and x == N - 1:
        cnt += 1
        return

    if d == 0:
        if x + 1 < N and not house[y][x + 1]:
            dfs(y, x + 1, 0)
        if x + 1 < N and y + 1 < N and not house[y + 1][x] and not house[y + 1][x + 1] and not house[y][x + 1]:
            dfs(y + 1, x + 1, 1)
    elif d == 1:
        if x + 1 < N and not house[y][x + 1]:
            dfs(y, x + 1, 0)
        if x + 1 < N and y + 1 < N and not house[y + 1][x] and not house[y + 1][x + 1] and not house[y][x + 1]:
            dfs(y + 1, x + 1, 1)
        if y + 1 < N and not house[y + 1][x]:
            dfs(y + 1, x, 2)
    elif d == 2:
        if x + 1 < N and y + 1 < N and not house[y + 1][x] and not house[y + 1][x + 1] and not house[y][x + 1]:
            dfs(y + 1, x + 1, 1)
        if y + 1 < N and not house[y + 1][x]:
            dfs(y + 1, x, 2)


# [ 입력 ]
N = int(input())  # 첫째 쭐에 집의 크기가 주어진다.
house = [list(map(int, input().split()))[:N] for _ in range(N)]
# 현재 위치에 따라 dfs 를 해주자. 0은 0도, 1은 45도, 2는 90도로 하자.
cnt = 0
dfs(0, 1, 0)
print(cnt)

```

