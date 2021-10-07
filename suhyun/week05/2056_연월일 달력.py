# 2056. 연월일 달력
m30 = [4, 6, 9, 11]
m31 = [1, 3, 5, 7, 8, 10, 12]


def solve(arr):
    # 년의 값 y
    y = ''.join(arr[0:4])
    # 달의 값 m
    m = ''.join(arr[4:6])
    # 날의값 d
    d = ''.join(arr[6:8])
    if int(m) in m30 and 1 <= int(d) <= 30:
        return y + '/' + m + '/' + d
    elif int(m) in m31 and 1 <= int(d) <= 31:
        return y + '/' + m + '/' + d
    elif int(m) == 2 and 1 <= int(d) <= 28:
        return y + '/' + m + '/' + d
    else:
        return -1


T = int(input())
for tc in range(1, T + 1):
    ymd = list(input())
    result = solve(ymd)
    print('#{} {}'.format(tc, result))
