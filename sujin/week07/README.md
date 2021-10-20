## 2112_보호필름 (49/50)

```python

def check():
    # 열별로 기준 충족하는지 체크하는 함수
    # 해당 열 기준 충족 >> 다음 열 >> 마지막열까지 충족하면 1
    for i in range(W):
        cnt = 1
        remember = -1
        for j in range(D):
            if remember == data[j][i]:
                cnt+=1
            else:
                cnt = 1
            # 검증기준 충족하면 다음 열로
            if cnt == K:
                break
            remember = data[j][i]
        # 한 열이라도 기준 미달이면 함수 종료
        if cnt < K:
            return 0
        
        
    # 모든 열 끝까지 검증 체크했으면 return 1
    return 1

def check2(val):
    # 약품 투입후 >> 열별로 기준 충족하는지 체크하는 함수
    # 해당 열 기준 충족 >> 다음 열 >> 마지막열까지 충족하면 is_break값을 val로
    # val : 약품 투입할 행 개수
    # selected : 고를 행 체크할 리스트
    # put : 고른 행에 어떤 약품을 넣을지 표시한 리스트

    global is_break
    # print(selected)
    # print(put)
    for i in range(W): # 열고르기
        cnt = 1
        pidx = 0
        remember = -1
        for j in range(D): # 해당 열, 한행씩 위에서부터 아래로
            # 해당 행이 선택된 행이면 
            if selected[j]: 
                # 이전 값과 put(약품 표시)와 비교
                # print(j,pidx)
                if remember == put[pidx]:
                    cnt += 1
                    remember = put[pidx]
                    pidx += 1
                else:
                    cnt = 1
                    remember = put[pidx]
                # 현재 값 저장 >>  다음 비교를 위해
                
            # 선택된 행 아니면 그냥 원래값으로 비교
            else:
                if remember == data[j][i]:
                    cnt+=1
                else:
                    cnt = 1 
                # 현재 값 저장 >>  다음 비교를 위해
                remember = data[j][i]
            # 검증기준 충족하면 다음 열로
            if cnt == K:
                break
             
        # 한 열이라도 기준 미달이면 함수 종료
        if cnt < K:
            return 
        # print(i,'열은 통과')
    # 모든 열 끝까지 검증 체크했으면 return 1
    is_break = val
    return 

def comb(idx,cnt,num):
    '''
    약품을 투입할 행을 고를 함수
    idx : 현재 포함 여부 선택할 행
    cnt : 포함한 행 개수 표시
    num : 고를 행 개수 1 <= num <= K
    '''

    # 열 다 골랐으면
    if cnt == num:
        # print(selected)
        comb2(0,num)

        # 이미 해당 선택 개수에서 답 나왔음 >> 종료
        if is_break:
            return     
        
    # 골라야할 행 개수 덜 골랐으면 return
    if idx == D:
        return  

    for i in range(2):
        selected[idx] = i
        comb(idx+1,cnt+i,num)
        if is_break:
            return 
        selected[idx] = 0 # 초기화

def comb2(idx,val):
    # A약품 넣을지 B약품 넣을지 행별로 중복순열로 나타낼 함수
    # val : 약품 투입할 행 개수
    global is_break

    if idx == val:
        check2(val)
        return
        
    for i in range(2):
        put[idx] = i
        comb2(idx+1,val)
        if is_break:
            return 



for tc in range(1, int(input())+1):
    # D : 보호필름 두께 , W : 보호필름 너비 , K : 합격기준
    D, W, K = map(int, input().split())
    # A : 0, B : 1
    data = [list(map(int, input().split())) for _ in range(D)]

    # 성능검사를 통과할 수 있는 약품의 최소 투입 횟수
    # 약품을 투입하지 않고도 성능검사를 통과하는 경우에는 0을 출력
    is_break = 0
    result = check()
    if result:
        print('#{} {}'.format(tc, 0))
    else:
        # 약품 투입이 필요하다면 >> 투입할 행 고르기
        # i : 투입할 행 개수, 투입 행 최대 개수는 K
        for i in range(1,K):
            # 고를 행 체크할 리스트
            selected = [0] * D
            # 어떤 약품 넣을지 표시할 리스트(A약품은 0, B약품은 1)
            put = [0]*i
            comb(0,0,i) # 약품을 투입할 행을 고를 함수
            
            if is_break:
                break
    
        if is_break:
            print('#{} {}'.format(tc,is_break))
        else:
            print('#{} {}'.format(tc,K))
        
        
```



## 14888_bkj_연산자끼워넣기

```python
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
```



## 2309_일곱난쟁이

```python
# 아홉 난쟁이 중 찐 일곱 난쟁이를 찾아 오름차순으로 출력
# 찐 일곱난쟁이 키의 합은 100

def comb(idx,height_sum):
    global is_true
    if idx == 7 and height_sum == 100:
        seven_man.sort()
        for e in seven_man:
            print(e)
        is_true = 1
        return 

    if idx == 7:
        return

    for i in range(9):
        if selected[i]:continue
        selected[i] = 1
        seven_man[idx] = height[i]
        comb(idx+1,height_sum+height[i])
        if is_true:return
        selected[i] = 0
        

height = []
for i in range(9):
    height.append(int(input()))
selected = [0] * 9
seven_man = [0]*7
is_true = 0
comb(0,0)
# print(height)
# print(selected)

```

