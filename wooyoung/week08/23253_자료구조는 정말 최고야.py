
# 교과서 갯수N, 교과서 더미 갯수M
# 문제 잘못읽어서 삽질..모모의 코드 봄~!
import sys
N, M = map(int, sys.stdin.readline().split())
for i in range(M):
    stack = []
    K = int(sys.stdin.readline())
    books = list(map(int, sys.stdin.readline().split()))
    for j in range(K):
        stack.append(books[j])
    if stack != sorted(stack, reverse=True):
        print('No')
        break
else:
    print('Yes')
