##  2112. 보호필름 

```python

```



###  14888. 연산자 끼워넣기

```python
# 14888. 연산자 끼워넣기
def dfs(n, total):
    global max_num, min_num
    if n == N:
        if total > max_num:
            max_num = total
        if total < min_num:
            min_num = total
        return
    # 더하기
    if ys[0]:
        ys[0] -= 1
        dfs(n + 1, total + num[n])
        ys[0] += 1
    # 빼기
    if ys[1]:
        ys[1] -= 1
        dfs(n + 1, total - num[n])
        ys[1] += 1
    # 곱하기
    if ys[2]:
        ys[2] -= 1
        dfs(n + 1, total * num[n])
        ys[2] += 1
    # 나누기
    if ys[3]:
        ys[3] -= 1
        # // 로 할 경우, 음수일때 정상작동하지않아, 우선 /를 해준후 int 형으로 변환시켜주었다.
        dfs(n + 1, int(total/num[n]))
        ys[3] += 1


N = int(input())  # 수의 개 수
num = list(map(int, input().split()))  # 숫자 나열
ys = list(map(int, input().split()))  # 연산자, N-1 개가 존재하며, 순서대로 더하기 뺴기 나누기 곱하기이다.

max_num = -1987654321
min_num = 1987654321

dfs(1, num[0])
print(max_num)
print(min_num)
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

```


