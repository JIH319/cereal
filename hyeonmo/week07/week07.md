# 2112. 보호필름

```python
# D : 보호 필름의 두께
# W : 가로 크기
# K : 합격 기준
# D줄에 걸쳐 셀들의 특성 W개가 주어진다 (A는 0, B는 1)

# dfs로 바꿔야 될 줄의 경우의 수를 순열로 들어가자
# 검사 안해도 되는 테스트 케이스도 있으니 함수 첫째줄에 검사부터 하는 가지치기 작성하자
# 검사하는 함수는 위에서 아래로 검사하자
# 순열은 A로 다 바꿨을때랑 B로 다 바꿨을때, 안바꾸고 넘어갈때를 고려하자
# 값을 바꿨다가 다시 돌아오는건 함수에 배열넣기 어려우니까 복사한 배열 하나를 따로 생성하고 거기서 값을 뺴오자


# import copy
def find_check():
    # 세로로 우선 검사
    for c in range(W):
        cnt = 0  # 한 세로줄에 몇개가 있는지
        cnt_key = 0  # 세로줄의 값이 연속된 값인지 확인하는 키값, 연속으로 세고있던 숫자가 0인지 1인지 확인 (내가 가지고있는 값)
        # 처음부터 값이 0이고 key가 0라면 그냥  cnt += 1
        # 그러다가 1이 나타나면 elif문 실행하고 key가 1로 바뀌고 cnt는 1로 초기화(이제 1을 연속으로 하는 값을 찾는다는 의미)
        for r in range(D):
            if film[r][c] == 0 and cnt_key == 1:
                cnt = 1
                cnt_key = 0
            elif film[r][c] == 1 and cnt_key == 0:
                cnt = 1
                cnt_key = 1
            else:
                cnt += 1
            if cnt == K:  # 이 줄은 더 볼필요 없다.(연속된 값 있음)
                break
            if r == D - K + 1 and cnt == 1:
                return 0

        else:

            return 0  # 한 줄에 연속된 값을 못찾음(실패),한줄이라도 못찾으면 0반환하고 끝내버리기
    return 1  # 모든 줄에 연속된 값이 존재함(성공,끝)


def dfs(cnt, start):
    global min_v

    if cnt >= min_v:
        return

    if cnt == K:
        min_v = cnt
        return

    # 검사하는 함수 실행 후 모든 줄에 연속된 값이 있다면 약품투입 횟수 최소값 찾기
    if find_check():
        if cnt < min_v:
            min_v = cnt
            return

    for i in range(start + 1, D):

        film_copy2 = film[i][:]

        film[i] = A
        dfs(cnt + 1, i)

        film[i] = B
        dfs(cnt + 1, i)

        film[i] = film_copy2



T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]

    A = [0 for _ in range(W)]
    B = [1 for _ in range(W)]

    min_v = 0xffff
    if K == 1:
        print('#{} {}'.format(tc, 0))
    else:
        dfs(0,-1)
        print('#{} {}'.format(tc, min_v))
```



---



# 14888. 연산자끼워넣기

```python
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
```