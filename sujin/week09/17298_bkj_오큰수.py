## 시간초과 

import sys
from collections import deque

N = int(sys.stdin.readline())
data = deque(map(int,sys.stdin.readline().split()))


for i in range(N-1):
    for j in range(i+1,N):
        # 왼쪽에서부터 차례로 비교후
        # 첫 큰 수 결과값으로 담고 break
        if data[j] > data[i]:
            print(data[j],end=' ')
            break 
    else:
        print(-1,end=' ')
print(-1)
