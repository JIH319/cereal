import sys

data = []
result = 0
N = int(sys.stdin.readline())
for i in range(N):
    temp = int(sys.stdin.readline().rstrip())
    # 새로 들어온 변수가 0이면, 리스트 마지막값 빼기
    if temp == 0 and data:
        result -= data.pop()
    # 0아니면 리스트에 담기
    else:
        result += temp
        data.append(temp)
print(result)
'''
import sys

data = ''
result = 0
N = int(sys.stdin.readline())
for i in range(N):
    data += sys.stdin.readline().rstrip()

stack = []
for j in range(N):
    # 맨 뒤 숫자가 아니라면, 뒷 숫자가 0인지 확인하고 더해줌
    if data[j] != '0':
        stack.append(int(data[j]))
    else:
        stack.pop()

print(sum(stack))
'''

