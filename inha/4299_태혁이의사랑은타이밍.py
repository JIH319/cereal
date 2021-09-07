T = int(input())

for tc in range(1, T+1):
    D, H, M = map(int, input().split())
    if D < 11:
        result = -1
    elif D == 11 and H < 11:
        result = -1
    elif D == 11 and H == 11 and M < 11:
        result = -1
    else:
        result = (D-11)*1440 + (H-11)*60 + (M-11)
    print('#{} {}'.format(tc, result))