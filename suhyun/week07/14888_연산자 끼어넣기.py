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
