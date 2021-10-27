# 2003. 수들의합2

```python
# N 개의 숫자들 i부터 j까지의 합이 M이 되는 경우의 수를 구하라
# 맨앞 인 i 위치 부터 합해서 M이 넘어가면 i+1 부터 다시 검사
# 시간초과로 pypy에서만 통과
N,M = map(int,input().split())
data = list(map(int,input().split()))
ans = 0

for i in range(N):
    sum_v = 0   # 경우의수 검사 할때마다 0으로 초기화
    for j in range(i,N):
        sum_v += data[j]
        if sum_v == M:   # M이 정확하게 맞아 떨어진다면 경우의 수 +1, break로 다음 경우의수 검사
            ans += 1
            break
        elif sum_v > M:  # 넘어간다면 break
            break

print(ans)




# 투 포인터 알고리즘을 이용하여 python 에서도 통과
# while 조건은 start가 end를 넘어가거나 end가 N보다 같거나 큰경우(넘어가는 경우) 종료
# start와 end가 같은 위치라면 start위치의 값만 sum_v에 할당
# start와 end 가 다른 위치라면 start부터 end까지의 값을 더해서 sum_v에 할당

# start와 end의 합이 M을 넘어버리고 start의 위치가 end보다 앞이라면 start를 1 증가한다.
# 그게 아니라면 계속해서 end를 1씩 증가하여 sum_v를 비교해준다.
'''
N,M = map(int,input().split())
data = list(map(int,input().split()))
ans = 0
start = 0
end = 0
while start <= end and end < N:
    if start == end:
        sum_v = data[start]
    else:
        sum_v = sum(data[start:end+1])
    if sum_v == M:
        ans += 1

    if sum_v > M and start < end:
        start += 1
    else:
        end += 1

print(ans)
'''
```



---



# 1949. 등산로조정

```python
def DFS(x,y,road,dump):
    global ans
    if road > ans:
        ans = road

    visited[x][y] = 1
    dx = [-1,0,1,0] # 상 우 하 좌
    dy = [0,1,0,-1] # 상 우 하 좌
  
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]

        if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
            # 현재 위치보다 가려는 곳이 작은값일때
            if arr[x][y] > arr[nx][ny]:
                DFS(nx,ny,road+1,dump)
            # 혹은 현재위치보다 높거나 같은 값일때는
            # 공사를 아직 안했고 현재값이 가려는곳을 공사한것보다 큰값이 된다면
            elif dump and arr[x][y] > arr[nx][ny] - K:
                tmp = arr[nx][ny]
                arr[nx][ny] = arr[x][y]-1
                DFS(nx,ny,road+1,0)
                arr[nx][ny] = tmp
    visited[x][y] = 0


T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_val = max(map(max,arr))

    visited = [[0]*N for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_val:
                DFS(i,j,1,1)
    print('#{} {}'.format(tc,ans))


```