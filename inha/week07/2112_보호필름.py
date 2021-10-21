import sys
sys.stdin = open('2112_input.txt')
# 셀 특성 A는 0, B는 1
# 출력: 약품을 투입해야하는 최소 투입 횟수


def check(arr): # 성능검사를 통과한 경우 1, 통과하지 못한 경우 0을 반환
    # 열 우선 순회
    for j in range(W):
        order = arr[0][j]
        cnt = 0
        for i in range(D):
            if arr[i][j] == order:
                cnt += 1
                if cnt == K:
                    break
            else:
                cnt = 1
                order = arr[i][j]
        else:
            # 성능통과 못 함
            return 0
    return 1


# 성능 검사 통과하지 못 했다면 약물 투입
def insert(idx, arr, cnt):  # idx: 약물 투입할 행의 인덱스, arr: 성능검사할 필름, cnt: 약물투입한 횟수
    global min_v
    # min_v보다 투입한 횟수가 많으면 return
    if cnt >= min_v:
        return
    # 성능검사 결과 통과 가능하면
    if check(arr):
        if min_v > cnt:
            min_v = cnt
        return
    # 마지막 행까지 약물을 투입해봤을 때 return
    if idx == D:
        return
    # 약물 투입한 행을 약물 투입 후에 다시 복구시키기 위해서 복사해둠
    temp = list(arr[idx])
    # 0: A 약물, 1: B 약물
    # idx 행에 A 약물 투입하거나
    arr[idx] = [0]*W
    insert(idx+1, arr, cnt+1)
    # idx 행에 B 약물 투입
    arr[idx] = [1]*W
    insert(idx+1, arr, cnt+1)
    arr[idx] = temp
    # 약물 투입 안 하거나
    insert(idx+1, arr, cnt)


for tc in range(1, int(input())+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    min_v = D
    if not check(film): # 통과하지 못하면
        insert(0, film, 0)  # 약물 투입
    else:   # 한번에 성능 검사 통과하면
        min_v = 0
    print('#{} {}'.format(tc, min_v))