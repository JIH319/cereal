# dfs로 재귀호출하여 모든 경우의 수를 구해보자
# 수열의 첫번쨰 값을 sum_v로 먼저 가지고 들어가고
# 이제 각 사칙연산에 계산을 해볼건데
# 사칙연산의 개수는 쓰면 한개씩 차감 쓰고 돌아올때 다시 원상태로 복구시킨다.
# k는 수열의 인덱스 i를 사칙연산의 인덱스로 사용한다.


def dfs(k,sum_v):
    global max_v
    global min_v

    if k == N: # 수열의 인덱스가 N과 동일하다면 수열 끝까지 다 계산해봄
        if sum_v > max_v:
            max_v = sum_v
        if sum_v < min_v:
            min_v = sum_v
        return

    for i in range(4):
        if data_math[i] == 0:   # 사용할수 있는 연산은 1 이상이다.
            continue
        if i == 0:
            data_math[i] -= 1
            dfs(k+1,sum_v+data_int[k])
            data_math[i] += 1
        elif i == 1:
            data_math[i] -= 1
            dfs(k + 1, sum_v-data_int[k])
            data_math[i] += 1
        elif i == 2:
            data_math[i] -= 1
            dfs(k + 1, sum_v*data_int[k])
            data_math[i] += 1
        elif i == 3:
            if sum_v < 0:
                # sum_v = -sum_v
                data_math[i] -= 1
                dfs(k + 1, -int(-sum_v/data_int[k]))    # 현재 값(sum_v)가 음수라면 양수로 바꾸고 나눈 몫을 다시 음수로 바꿔주고 넘긴다.
                data_math[i] += 1

            else:
                data_math[i] -= 1
                dfs(k + 1, int(sum_v / data_int[k]))
                data_math[i] += 1



N = int(input())
data_int = list(map(int,input().split()))
data_math = list(map(int,input().split()))
first_data = data_int[0]
max_v = -0xffffffff
min_v = 0xfffffffff

# data_math[0] = '+'
# data_math[1] = '-'
# data_math[2] = '*'
# data_math[3] = '//'

dfs(1,first_data)
print(max_v)
print(min_v)

