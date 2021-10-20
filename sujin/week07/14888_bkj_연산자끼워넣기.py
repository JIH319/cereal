import sys
from collections import deque

def calc():
    '''
    num : 연산자 개수
    '''
    global minV, maxV,cnt
    cnt += 1
    numbers = number.copy()
    # 들어온 연산자 순서대로 연산 진행 >> 최대값 최소값 갱신
    for i in range(N-1): # N : 숫자의 수 >> 연산자 개수 : N-1
    
        n1 = numbers.popleft()
        n2 = numbers.popleft()
        # 연산자 0 : +, 1 : -, 2: * , 3: //
        op = operator[i]
        
        if op == 0: # 덧셈
            tmp = n1+n2
            # 한번이라도 중간에 범위 벗어나면 함수종료
            if -1000000000 > tmp or tmp > 1000000000:return
            numbers.appendleft(tmp)
        elif op == 1: # 뺼셈
            tmp = n1-n2
            if -1000000000 > tmp or tmp > 1000000000:return
            numbers.appendleft(tmp)
        elif op == 2: # 곱셈
            tmp = n1*n2
            if -1000000000 > tmp or tmp > 1000000000:return
            numbers.appendleft(tmp)
        else: # 나눗셈
            if n1 < 0 and n2 >= 0:
                tmp = (-n1) // n2
                tmp = -tmp
            else:
                tmp = n1//n2
            if -1000000000 > tmp or tmp > 1000000000:return
            numbers.appendleft(tmp)
    
    if numbers[0] < minV:
        minV = numbers[0]
    if numbers[0] > maxV:
        maxV = numbers[0]
    return


def perm(idx,num):
    '''
    idx : 자리 확정 지으려고 하는 인덱스위치
    num : 연산자 개수 >> 자리 확정할 개수
    '''
    # 순열완성 >> 계산시도
    if idx == num:
        calc()
        return

    for i in range(idx,num):
        operator[i],operator[idx] = operator[idx],operator[i]
        perm(idx+1,num)
        operator[i],operator[idx] = operator[idx],operator[i] # 되돌리기
# 수의 개수
N = int(sys.stdin.readline())
# 연산 진행 과정에서 숫자들을 담을 deque
number = deque(map(int,sys.stdin.readline().split()))
data = list(map(int, sys.stdin.readline().split()))

# 연산자 0 : +, 1 : -, 2: * , 3: // 
operator = []
for i in range(4):
    operator_num = data[i]  # 해당 연산자의 개수
    for _ in range(operator_num):
        operator.append(i)
# 식의 결과가 최대인 것과 최소
# -10억이상 10억이하, 중간과정 포함
minV = 1000000001
maxV = -10000000001
cnt = 0
perm(0,N-1) # 인덱스 위치, 연산자 개수 

print(maxV)
print(minV)

