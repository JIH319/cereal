## 1. boj14888_연산자 끼워넣기 

```python
# N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.
# 6
# 1 2 3 4 5 6
# 2 1 1 1


def dfs(idx, tmp):
    global max, min
	
    # 모든 숫자들로 식을 만들었다면
    if idx == n - 1:
        # 결과값이 최대값보다 큰 경우
        if tmp > max:
            max = tmp
        # 결과값이 최소값보다 작은 경우
        if tmp < min:
            min = tmp
        return

    # 더하기가 1개 이상 있는 경우
    if v[0] > 0: 
        # 더하기 갯수 -1
        v[0] -= 1 
        # 다음 숫자들을 연산하기 위한 idx 이동, (지금까지 연산 결과값 + 현재 숫자)
        dfs(idx+1, tmp + nums[idx+1]) 
        # 모든 조합을 확인하기 위해서 원상복귀
        v[0] += 1

    # 빼기가 1개 이상 있는 경우
    if v[1] > 0:
        # 빼기 갯수 -1
        v[1] -= 1
        # 다음 숫자 연산하기 위해 idx 이동, (지금까지 연산 결과값 - 현재 숫자)
        dfs(idx+1, tmp - nums[idx+1]) # (1, 1+2)
        # 모든 조합을 확인하기 위해서 원상복귀
        v[1] += 1

    # 곱하기 1개 이상 있는 경우
    if v[2] > 0: 
        v[2] -= 1
        dfs(idx+1, tmp * nums[idx+1]) # (1, 1+2)
        v[2] += 1
        
    # 나누기 1개 이상 있는 경우
    if v[3] > 0:
        v[3] -= 1
        if tmp < 0:
            dfs(idx+1, (abs(tmp) // nums[idx+1]) * -1) # (1, 1+2)
            v[3] += 1

        else:
            dfs(idx+1, tmp // nums[idx+1]) # (1, 1+2)
            v[3] += 1

# n : 숫자의 갯수, nums : 숫자들, v = 연산자들
n = int(input()) 
nums = list(map(int,input().split()))
v = list(map(int,input().split()))
result = ''
max = -0xfffffffffffffffffff
min = 0xfffffffffffffffffff
# (숫자 사이 첫 idx, 만들 수 있는 식의 결과 = 아직 연산한게 없어서 0번째 숫자) 
dfs(0, nums[0])

print(max)
print(min)
```



## 2. swea2112_보호필름

```python
# 이 조합으로 검사를 통과할 수 있는가?
def check_arr(tmp_corp, tmp):
    # 조합대로 배열 바꿔주기
    for i in range(D):
        # A로 바꾸는 조합이라면, 해당 행의 모든 열들을 A로 바꿔주자
        if tmp_corp[i] == 2:
            for a in range(W):
                tmp[i][a] = 0
        # B로 바꾸는 조합이라면, 해당 행의 모든 열들을 B로 바꿔주자
        if tmp_corp[i] == 3:
            for b in range(W):
                tmp[i][b] = 1

    # 바꾼 열이 강화유리 조건에 맞는지 확인!
    total_cnt = 0
    for d in range(D):
        # 나 자신 포함 연속된 숫자이기 때문에 나는 1
        cnt = 1
        # w열의 각 행들에서 K개 이상 연속된 숫자가 나온 경우 break
        for w in range(W-1):
            # 만약 연속된 숫자가 나온다면 cnt += 1
            if tmp[d][w] == tmp[d][w+1]:
                cnt += 1
            # 연속하지 않은 경우 cnt = 1로 초기화
            else:
                cnt = 1

        if cnt >= K:
            total_cnt += 1
            break

    if total_cnt == D:
        return 'True'
    else:
        return 'False'

# 조합 만드는 함수
def solve(idx):
    global min_val
    # 길이가 D인 하나의 조합이 만들어 졌으면
    if idx == D:
        ans = 0
        # 2. 이 조합으로 조건이 충족하는지 확인하고, 충족하는경우에
        if check_arr(corp, arr) == 'True':
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
    min_val = 100000             #최소 움직인 횟수
    corp = [0] * D
    solve(0)

    print(f'#{tc} {min_val}')
```

