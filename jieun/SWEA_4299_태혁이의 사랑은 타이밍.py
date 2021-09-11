T = int(input())
for tc in range(1,T+1):
    D, H, M = map(int, input().split())
    result = (D - 11)*1440 + (H - 11)*60 + (M - 11)
    if result < 0 :
        print('#{} {}'.format(tc, -1))
    else:
        print('#{} {}'.format(tc, result))