# 1213. 팰린드롬 만들기
```python
def palindrome():
    check = ''
    answer_list = []
    for k, v in munza.items():
        if v % 2:
            if check:
                return 'I\'m Sorry Hansoo'
            check = k
            for _ in range(v//2):
                answer_list.append(k)
        else:
            for _ in range(v//2):
                answer_list.append(k)
    answer_list.sort()
    return ''.join(answer_list) + check + ''.join(answer_list[::-1])


munza = {}

for char in input():
    if char in munza.keys():
        munza[char] += 1
    else:
        munza[char] = 1

print(palindrome())
```

# 17070. 파이프 옮기기
## DFS - pypy로 간당간당
```python
import sys
input = sys.stdin.readline


def dfs(y, x, pos):
    global ans

    if pos == 1:
        # 가로 이동
        if 0 <= x+1 < n and not house[y][x+1]:
            if y == n - 1 and x+1 == n - 1:
                ans += 1
            else:
                dfs(y, x+1, 1)
        # 대각선 이동
        if y + 1 < n and x + 1 < n and not house[y][x + 1] and not house[y + 1][x + 1] and not house[y + 1][x]:
            if y + 1 == n - 1 and x + 1 == n - 1:
                ans += 1
            else:
                dfs(y + 1, x + 1, 3)

    elif pos == 2:
        # 세로 이동
        if y+1 < n and not house[y+1][x]:
            if y+1 == n-1 and x == n-1:
                ans +=1
            else:
                dfs(y+1, x, 2)
        # 대각선 이동
        if y + 1 < n and x + 1 < n and not house[y][x+1] and not house[y+1][x+1] and not house[y+1][x]:
            if y+1 == n - 1 and x+1 == n - 1:
                ans += 1
            else:
                dfs(y + 1, x + 1, 3)

    elif pos == 3:
        # 세로 이동
        if y+1 < n and not house[y+1][x]:
            if y+1 == n-1 and x == n-1:
                ans +=1
            else:
                dfs(y+1, x, 2)
        # 가로 이동
        if x+1 < n and not house[y][x+1]:
            if y == n - 1 and x+1 == n - 1:
                ans += 1
            else:
                dfs(y, x+1, 1)
        # 대각선 이동
        if y + 1 < n and x + 1 < n and not house[y][x+1] and not house[y+1][x+1] and not house[y+1][x]:
            if y+1 == n - 1 and x+1 == n - 1:
                ans += 1
            else:
                dfs(y + 1, x + 1, 3)


# 1: 가로, 2: 세로, 3: 대각선
n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

ans = 0
dfs(0, 1, 1)
print(ans)

```

## DP
```python
n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

check_dict = {0: (0, 2), 1: (1, 2), 2: (0, 1, 2)}
pos_dict = {0: (0, 1), 1: (1, 0), 2: (1, 1)}
ans = 0
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for i in range(n):
    for j in range(n):
        for k in range(3):
            if dp[i][j][k] and not house[i][j]:  # 해당 방향으로 파이프가 놓이는 방법이 있고, 벽이 없음
                for x in check_dict[k]:
                    ny = i + pos_dict[x][0]
                    nx = j + pos_dict[x][1]
                    if ny < n and nx < n and not house[ny][nx]:
                        if x != 2: # 대각선이 아니라면
                            dp[ny][nx][x] += dp[i][j][k]
                        else: # 대각선이라면
                            if not house[ny-1][nx] and not house[ny][nx-1]:
                                dp[ny][nx][x] += dp[i][j][k]


print(sum(dp[n-1][n-1]))
```
