## #4223 삼성이의 트라우마 극복

```python
def ptsd(temp):
    
    if len(temp) < 7 or temp.count('S') < 2 or temp.count('A') < 1 or temp.count('M') < 1 or temp.count('U') < 1 or temp.count('N') < 1 or temp.count('G') < 1:
        return 0
    return 1
    
T = int(input())
for tc in range(1,T+1):
    N = int(input())        # 심사위원 수
    data = []
    datacheck = []
    for i in range(N):
        length = int(input())
        name = input().split()
        datacheck += name
        score = int(input())
        data.append([score,name])
    # 심사위원 이름 안에서 삼성 만들수있는지 없는지 체크
    datacheck = ptsd(datacheck)
    result = 1001*N
    j = 1
    #  powerset
    while datacheck and j < 2**N:
        temp = []
        temp_sum = 0
        for k in range(N):
            # 리스트에 포함 할 말
            if j & (1 << k) != 0:
                temp += data[k][1]  # 이름
                temp_sum += data[k][0]  # 점수
        j += 1
        # 현재 삼성 만들 수 있는 조합의 최소합보다 커지면 그냥 이 조합 계산도 하지말기
        if temp_sum >= result:
            continue
        # 삼성 글자 만들수 없다면,
        if not ptsd(temp):
            continue
        # 삼성 글자 만들 수 있다면,
        else:
            
            result = temp_sum
    
    # 삼성글자 만들 수 있을 때 result : 최소합
    if result != 1001*N:
        print('#{} {}'.format(tc,result))
    else:
        print('#{} {}'.format(tc,-1))                
```

---





## 2667_bkj_단지번호붙이기

```python
import sys

def bfs(r,c):
    # 같은 단지에는 같은 숫자(1과 혼동하지 않기 위해 2부터)를 붙여준다
    global num
    num += 1
    visited[r][c] = num
    # 단지 내 주택 수 세기
    cnt = 1
    q = []
    q.append((r,c))
    while q:
        cr, cc = q.pop()
        # 집은 상우하좌 네가지 방향으로만 인정
        for di, dj in [(-1,0),(0,1),(1,0),(0,-1)]:
            nr, nc = cr+di, cc+dj
            if 0<=nr<N and 0<=nc<N and arr[nr][nc] and not visited[nr][nc]:
                q.append((nr,nc))
                visited[nr][nc] = num
                cnt += 1
    return cnt  

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
num = 1
result = []
for i in range(N):
    for j in range(N):
        # 주택이 있고, 다른 단지에 포함되지 않은 주택이면 
        if arr[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i,j))

print(num-1)
result.sort()
for e in result:
    print(e)
```

---

## #10814_bkj_나이순정렬

```python
import sys
N = int(sys.stdin.readline())
data = {}
age_list = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    # 나이만 담는 리스트 생성(중복X)
    if age not in age_list:
        age_list.append(age)
    # 나이를 키로 하는 딕셔너리 
    if age in data:
        data[age].append(name)
    else:
        data[age] = [name]
# 가장 작은 나이부터 나이목록에서 추출
while age_list:
    temp = min(age_list)
    temp_list = data[temp]
    # 해당 나이의 이름을 순서대로 출력
    for e in temp_list:
        print('{} {}'.format(temp, e))
    age_list.remove(temp)
```

