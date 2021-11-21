# N개의 에너지 구슬
# 두번째 입력값은 에너지 구슬의 무게
# 1. 에너지 구슬 하나를 고른다.
# 2. 고른 에너지 구슬을 제거한다.
# 3. 에너지 구슬을 고를때 첫번째와 마지막구슬은 고를수 없다.
# 4. 제거한 에너지 구슬 양옆의 구슬의 에너지를 곱한 값을 result에 저장한다.
# 5. N을 1 감소시키고 처음부터 다시 에너지구슬을 고른다.
# 위의 조건으로 에너지를 구할때 구할수 있는 에너지양의 최대값을 출력하라
# 재귀

def solve(N):
    global sum_v
    global max_v
    if N == 2:
        if sum_v > max_v:
            max_v = sum_v
            return


    for i in range(1,N-1):
        sum_v += data[i-1] * data[i+1]
        x = data.pop(i)
        solve(N-1)
        data.insert(i,x)
        sum_v -= data[i - 1] * data[i + 1]

N = int(input())
data = list(map(int,input().split()))
sum_v = 0
max_v = -1
solve(N)
print(max_v)