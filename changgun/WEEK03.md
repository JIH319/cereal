### 백준/10814/나이순 정렬

```python
n = int(input())
names = [input() for _ in range(n)]
names.sort(key=lambda x: int(x.split()[0]))
print(*names, sep='\n')
```



### 백준/2556/단지번호

```python
def dfs(i, j):
    global cnt
    # 유효성 검사
    if i not in range(n) or \
        j not in range(n) or \
        grid[i][j] != 1:
        return
    
    cnt += 1
    grid[i][j] = 0
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)


# 지도의 크기(n), 2차원 배열 형태의 지도(grid)
n = int(input())
grid = [list(map(int, list(input()))) for _ in range(n)]

# 단지 수를 세아리는 변수
dangi_cnt = 0
# 개별 단지내의 집의 수를 보관할 리스트
house_cnt = list()
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            cnt = 0
            dfs(i, j)
            dangi_cnt += 1
            house_cnt.append(cnt)
# 오름차순
house_cnt.sort()
# 출력            
print(dangi_cnt)
print(*house_cnt, sep='\n')
```



