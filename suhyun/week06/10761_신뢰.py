# 10761. 신뢰
def search():
    # bi는 blue 의 현재 위치, oi 는 orange 의 현재 위치
    bi = oi = 0
    rst = 0
    while len(blue) != 0 or len(orange) != 0:
        # 처음 오더가 blue 일 때,
        if robots[0] == 'B':
            if int(robots[1]) - 1 > bi:
                bi += 1
            elif int(robots[1]) - 1 < bi:
                bi -= 1
            # bi 가 일치할 경우, robots 와 blue 의 위치 값을 모두 제거해주자.
            else:
                robots.pop(0)
                robots.pop(0)
                blue.pop(0)

            # orange 도 눌러야될게 있을 경우,
            if len(orange) != 0:
                if oi < orange[0] - 1:
                    oi += 1
                elif oi > orange[0] - 1:
                    oi -= 1
        else:
            if int(robots[1]) - 1 > oi:
                oi += 1
            elif int(robots[1]) - 1 < oi:
                oi -= 1
            # oi 가 일치할 경우, robots 와 orange 의 위치 값을 모두 제거해주자.
            else:
                robots.pop(0)
                robots.pop(0)
                orange.pop(0)

            # blue 도 아직 남아있을 경우,
            if len(blue) != 0:
                if bi < blue[0] - 1:
                    bi += 1
                elif bi > blue[0] - 1:
                    bi -= 1
        rst += 1
    return rst


T = int(input())  # 테스트 케이스의 수 T
for tc in range(1, T + 1):
    robots = list(map(str, input().split()))
    N = int(robots.pop(0))
    blue = []
    orange = []
    for p in range(0, len(robots) - 1, 2):
        if robots[p] == 'B':
            blue.append(int(robots[p + 1]))
        else:
            orange.append(int(robots[p + 1]))
    result = search()
    print('#{} {}'.format(tc, result))
