import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

s, e = 0, 0
num_sum, cnt = 0, 0
for s in range(N):
    while num_sum < M and e < N:
        num_sum += nums[e]
        e += 1
    if num_sum == M:
        cnt += 1
    num_sum -= nums[s]

print(cnt)