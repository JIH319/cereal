import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 리스트에 nums 첫번째 요소를 저장함
sum_lst = [nums[0]]
# 0부터 i 번째까지의 누적 합계를 sum_lst에 저장
for i in range(N-1):
    sum_lst.append(sum_lst[i]+nums[i+1])

cnt = 0
# 수열을 더해서 M이 될 수 있는 것을 찾음
for j in range(N-1, -1, -1):
    if sum_lst[j] > M:
        for i in range(j-1, -1, -1):
            num_sum = sum_lst[j] - sum_lst[i]
            if num_sum == M:
                cnt += 1
                break
            elif num_sum > N:
                break
    elif sum_lst[j] == M:
        cnt += 1

print(cnt)

