# 시간초과
# 스택으로 어떻게 풀어야될지 모르겠어요,,
import sys
input = sys.stdin.readline


def nge(numbers, idx):
    base = numbers[idx]
    for i in range(idx+1, N):
        if base < numbers[i]:
            return numbers[i]
    return -1


N = int(input())
nums = list(map(int, input().split()))
for i in range(N):
    result = nge(nums, i)
    print(result, end=' ')
print()