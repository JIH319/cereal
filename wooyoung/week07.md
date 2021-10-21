## 1. boj14888_연산자 끼워넣기 

```python
# N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.
# 6
# 1 2 3 4 5 6
# 2 1 1 1
def dfs(idx, tmp):
    global max, min

    if idx == n - 1:
        if tmp > max:
            max = tmp
        if tmp < min:
            min = tmp
        return

    if v[0] > 0: # 더하기가 1이상인 경우
        v[0] -= 1 # 더하기 갯수 -1
        dfs(idx+1, tmp + nums[idx+1]) # (1, 1+2)
        v[0] += 1

    if v[1] > 0: # 뻬기 1이상인 경우
        v[1] -= 1
        dfs(idx+1, tmp - nums[idx+1]) # (1, 1+2)
        v[1] += 1

    if v[2] > 0: # 곱하기
        v[2] -= 1
        dfs(idx+1, tmp * nums[idx+1]) # (1, 1+2)
        v[2] += 1

    if v[3] > 0:
        v[3] -= 1
        if tmp < 0:
            dfs(idx+1, (abs(tmp) // nums[idx+1]) * -1) # (1, 1+2)
            v[3] += 1

        else:
            dfs(idx+1, tmp // nums[idx+1]) # (1, 1+2)
            v[3] += 1


n = int(input()) # 숫자의 갯수
nums = list(map(int,input().split()))
v = list(map(int,input().split()))
result = ''
max = -0xfffffffffffffffffff
min = 0xfffffffffffffffffff
dfs(0, nums[0])

print(max)
print(min)
```



## 2. swea2112_보호필름

```python
# 이 조합으로 검사를 통과할 수 있는가?
def check_arr():
    # 조합대로 배열 바꿔주기
    for i in range(D):
        # A로 바꾸는 조합이라면, 해당 행의 모든 열들을 A로 바꿔주자
        if corp[i] == 2:
            for a in range(W):
                arr[i][a] = 0
        # B로 바꾸는 조합이라면, 해당 행의 모든 열들을 B로 바꿔주자
        if corp[i] == 3:
            for b in range(W):
                arr[i][b] = 1

    # 바꾼 열이 강화유리 조건에 맞는지 확인!
    total_cnt = 0
    for d in range(D):
        # 나 자신 포함 연속된 숫자이기 때문에 나는 1
        cnt = 1
        # w열의 각 행들에서 K개 이상 연속된 숫자가 나온 경우 break
        for w in range(W-1):
            if cnt >= K:
                total_cnt += 1
                break
            # 만약 연속된 숫자가 나온다면 cnt += 1
            if arr[d][w] == arr[d][w+1]:
                cnt += 1
            # 연속하지 않은 경우 cnt = 1로 초기화
            else:
                cnt = 1

    if total_cnt == D:
        return 'True'
    else:
        return 'False'

# 조합 만드는 함수
def solve(idx):
    global min_val
    ans = 0
    # 길이가 D인 하나의 조합이 만들어 졌으면
    if idx == D:
        # 2. 이 조합으로 조건이 충족하는지 확인하고, 충족하는경우에
        if check_arr() == 'True':
            # A 또는 B로 바꾼 횟수가 몇번인지 확인후에
            for j in range(D):
                if corp[j] == 1:
                    ans += 1
                if corp[j] == 2:
                    ans += 1
            # 바꾼 횟수가 최소횟수보다 작은 경우, 최소 바꾼 횟수!
            if min_val > ans:
                min_val = ans
        return

    for i in range(3):
        if v[idx] == 0:
            v[idx] = 1
            corp[idx] = dir[i]
            solve(idx+1)
            v[idx] = 0

T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split()) # 세로크기 D , 가로크기 W, 합격기준 연속갯수 K
    arr = [list(map(int,input().split())) for _ in range(D)]
    # 1. 조합 만들기
    v = [0] * D                     #방문 check
    dir = [1,2,3]                   # 1: 그대로, 2: 0으로바꾸기, 3: 1로 바꾸기
    min_val = 0xffffff              #최소 움직인 횟수
    corp = [0] * D

    # 조합
    my_arr = arr
    solve(0)

    print(f'#{tc} {min_val}')
```

