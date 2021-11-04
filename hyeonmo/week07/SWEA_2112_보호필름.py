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









##############################################################################
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


def dfs(cnt):
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

    for i in range(cnt, D):
        if used[i] == 1:
            continue
        used[i] = 1
        film_copy2 = film[i][:]

        film[i] = A
        dfs(cnt + 1)

        film[i] = B
        dfs(cnt + 1)

        film[i] = film_copy2
        used[i] = 0


T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    A = [0 for _ in range(W)]
    B = [1 for _ in range(W)]
    used = [0] * D
    min_v = 0xffff
    if K == 1:
        print('#{} {}'.format(tc, 0))
    else:
        dfs(0)
        print('#{} {}'.format(tc, min_v))