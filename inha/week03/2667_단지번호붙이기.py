import sys
input = sys.stdin.readline


def house(start):
    stack = [start]
    arr[start[0]][start[1]] = 0
    cnt = 1
    while stack:
        ci, cj = stack[-1][0], stack[-1][1]
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == '1':
                arr[ni][nj] = 0
                stack.append([ni, nj])
                cnt += 1
                break
        else:
            stack.pop()
    return cnt


N = int(input())
arr = [list(input()) for _ in range(N)]
cnt = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            start = [i, j]
            cnt.append(house(start))

cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)

# 6
# 010011
# 111011
# 010011
# 000001
# 001101
# 001001