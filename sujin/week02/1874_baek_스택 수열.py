

'''
import sys
N = int(sys.stdin.readline())
data = ''
for i in range(N):
    data += sys.stdin.readline().rstrip()

stack = ''
result = ''
dataidx = 0
for j in range(1,N+1):
    stack += str(j)
    result += '+'
    # 일단 넣고, 해당 숫자 (i)가 나올 순서면 pop 
    while stack and stack[-1] == data[dataidx]:
         stack = stack[:-1]
         result += '-'
         dataidx += 1

if dataidx == N and not stack:
    print('\n'.join(result))
else:
    print('NO')



import sys
N = int(sys.stdin.readline())
data = ''
for i in range(N):
    data += sys.stdin.readline().rstrip()

stack = []
result = ''
dataidx = 0
for j in range(1,N+1):
    stack.append(j)
    result += '+'
    # 일단 넣고, 해당 숫자 (i)가 나올 순서면 pop 
    while stack and stack[-1] == int(data[dataidx]):
         stack.pop()
         result += '-'
         dataidx += 1

if dataidx == N and not stack:
    print('\n'.join(result))
else:
    print('NO')

'''


# for k in range(2*N):
    #     print(result[k])

import sys
N = int(sys.stdin.readline())
data = ''
for i in range(N):
    data += sys.stdin.readline().rstrip()

stack = []
result = ''
dataidx = 0
for j in range(1,N+1):
    # 일단 넣고, 해당 숫자 (i)가 나올 순서면 pop 
    while j <= int(data[dataidx]):
        stack.append(j)
        result += '+'
        if j == int(data[dataidx]):
            stack.pop()
            result += '-'
            dataidx += 1

if dataidx == N and not stack:
    print('\n'.join(result))
else:
    print('NO')