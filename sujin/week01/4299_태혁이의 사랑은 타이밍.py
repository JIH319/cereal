def prayforhim(D, H, M):
    timing = (D-1) * 24 * 60 + H * 60 + M   # 깨달은 순간까지의 분
    promise = 10 * 24 * 60 + 11 * 60 + 11   # 약속시간까지의 분
    result = timing - promise
    if result < 0:
        return -1
    else:
        return result

for tc in range(1,int(input())+1):
    D, H, M = map(int, input().split())
    print('#{} {}'.format(tc,prayforhim(D, H, M)))