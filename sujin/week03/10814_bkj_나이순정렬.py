'''
import sys
N = int(sys.stdin.readline())
data = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    data.append((age, name))
for j in range(N-1,0,-1):
    for k in range(0,j):
        if data[k][0] > data[k+1][0]:
            data[k],data[k+1] = data[k+1],data[k]
for e in data:
    print(' '.join(e))
'''

'''
import sys
N = int(sys.stdin.readline())
data = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    data.append((age, name))
data.sort(key=lambda x:x[0])
for e in data:
    print(' '.join(e))
'''
'''

import sys
N = int(sys.stdin.readline())
data = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    # 첫번째 원소
    if not data:
        data.append((age, name))
        continue
    # 리스트 원소 존재시 비교후 삽입
    for i in range(len(data)):
        if data[i][0] > age:
            data.insert(i, (age, name))
            break
    # 리스트 가장 마지막수의 같거나 그보다 클 경우
    else:
        data.append((age, name))
for e in data:
    print(' '.join(e))
'''

import sys
N = int(sys.stdin.readline())
data = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    data.append((age, name))
for j in range(N-1,0,-1):
    for k in range(0,j):
        if data[k][0] > data[k+1][0]:
            data[k],data[k+1] = data[k+1],data[k]
for e in data:
    print(' '.join(e))