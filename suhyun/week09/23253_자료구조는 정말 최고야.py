# 23253. 자료구조는 정말 최고야
import sys
N, M = map(int, input().split())  # N : 교과서의 수 , M : 교과서 더미의 수 M

is_valid = 'Yes'
for _ in range(M):
    k = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))[:k]
    if arr != sorted(arr,reverse=True):
        is_valid='No'
        break
print(is_valid)
