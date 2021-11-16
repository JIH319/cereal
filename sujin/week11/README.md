## 6603_bkj_로또

```python
'''
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
'''
# k(k>6)개의 수를 골라 집합 S를 만든 다음 그 수만 가지고 번호를 선택
# 첫 번째 수는 k (6 < k < 13)이고, 
# 다음 k개 수는 집합 S에 포함되는 수이다. 
# S의 원소는 오름차순으로 주어진다.
# 입력의 마지막 줄에는 0이 하나 주어진다. 
# 사전 순으로 출력/ 테케 한줄 비우기

def comb(idx, cnt):
    '''
    idx : 현재 고를지말지 정할 인덱스
    cnt : 현재 고른 숫자의 개수 (6 될때까지 함수 재귀호출)
    '''
    # 6개 골랐으면 출력
    if cnt == 6:
        for i in range(N):
            if selected[i]:
                print(data[i],end=' ')
        print()
        return

    # 인덱스끝까지 왔으면 더이상 X
    if idx == N:
        return

    # 사전순 출력을 위해 일단 선택(1) > (0)
    for i in range(1,-1,-1):
        selected[idx] = i
        comb(idx+1,cnt+i)
        selected[idx] = 0
    pass

while True:
    data = list(map(int,input().split()))
    N = int(data.pop(0))
    # input 0 들어올때까지 반복
    if N == 0:
        break
    # selected : 선택 표시
    selected = [0]*N
    comb(0,0)
    print()
```





## 11399_bkj_ATM

```python
N = int(input())
data = list(map(int,input().split()))
data.sort() # 오름차순 정렬
for i in range(1,N):
    # 누적합
    data[i] = data[i-1] + data[i]
print(sum(data))
```







## 16198_bkj_에너지모으기

```python
# 고른 에너지 구슬의 번호를 x라고 한다. 
# 단, 첫 번째와 마지막 에너지 구슬은 고를 수 없다.
# x번째 에너지 구슬을 제거한다.
# Wx-1 × Wx+1의 에너지를 모을 수 있다.
# N을 1 감소시키고, 에너지 구슬을 1번부터 N번까지로 다시 번호를 매긴다. 
'''
4
1 2 3 4
#12

5
100 2 1 3 100
#10400
'''
def calc():
    global maxV
    energy = 0
    for i in range(1,N-1):
        # idx : i번째로 뺄 구슬의 위치
        idx = 0
        for j in range(1,N-1):
            # 순서가 i번째인 구슬의 위치 j 찾기
            if order[j] == i:
                idx = j
                break
        tmp = idx-1
        # order가 더 작다 == 이미 먼저 뺀 구슬
        while order[tmp] < order[idx]:
            tmp -= 1
        if tmp == 0:
            val1 = data[0]
        else:
            val1 = data[tmp]

        tmp = idx+1
        while order[tmp] < order[idx]:
            tmp += 1
        if tmp == N-1:
            val2 = data[N-1]
        else:
            val2 = data[tmp]

        energy += val1 * val2
     
    maxV = max(maxV,energy)
    
# 순열만들기
def perm(idx):

    if idx == N-1:
        # print(order)
        calc()
        return

    for i in range(1,N-1):
        if selected[i] == 0:
            order[idx] = i
            selected[i] = 1
            perm(idx+1)
            selected[i] = 0

N = int(input())
data = list(map(int,input().split()))
# order : 순서 표시할 배열 / index : 구슬 순서, val : 뽑을 구슬 번호
selected = [0] *(N-1) 
order = [987654321]*N
maxV = 0
perm(1)
print(maxV)
```



## 1931_bkj_회의실배정

```python
'''
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
#4
'''
# 각 회의 I에 대해 시작시간과 끝나는 시간
# 한 회의가 끝나는 것과 동시에 다음 회의가 시작 가능

def timeTable():
    start = 0
    cnt = 0
    for i in range(N):
        # 시작시간이 이전 회의보다 같거나 늦게
        if time[i][0] >= start:
            # 회의마치는시간을 start에 넣어줌 >> 다음 회의 시작시간과 비교
            start = time[i][1]
            cnt += 1
    print(cnt)

import sys

N = int(sys.stdin.readline())
time = []
for _ in range(N):
    s,e = map(int,sys.stdin.readline().split())
    time.append((s,e))
# 끝나는 시간이 이른 순으로 정렬
# ??? 틀리길래 마치는시각 같은것들 사이에서도 정렬이 필요한가해서
# x[0] 추가했더니 맞았다...테케 뭘까...?....
time.sort(key=lambda x:(x[1],x[0])) 
timeTable()
```





## 18222_bkj_투에-모스 문자열

```python
import sys
# from collections import deque
# 자연수 k가 주어졌을 때 X의 k번째에는 무슨 문자가 오는지 구하여라.
K = int(sys.stdin.readline())

tmp = K
# 맨처음 0으로부터 몇번 나아갔는지 셀 변수
cnt =  0
# K번째 수부터 거꾸로 0까지 반복
while tmp:  
    i = 0
    # tmp보다 작은 수 중 가장 큰 2의 배수를 빼준다
    while tmp > 2**i:
        i += 1
    if i == 0:  # tmp가 1이 되었을때
        tmp = 0
    else:
        tmp -= 2**(i-1)

    cnt += 1    # 0에서부터 한번 더 나아갔다고 +1
    
if cnt%2:
    print(0)
else:
    print(1)
    
#################################################33

import sys

def calc(tmp):
    global cnt
    if tmp <= 1:
        cnt += 1
        return
    
    i = 0
    # tmp보다 작은 수 중 가장 큰 2의 배수를 빼준다
    while tmp > 2**i:
        i += 1
    if i == 0:  # tmp가 1이 되었을때
        tmp = 0
    else:
        tmp -= 2**(i-1)
    cnt += 1    # 0에서부터 한번 더 나아갔다고 +1
    
    calc(tmp)
# from collections import deque
# 자연수 k가 주어졌을 때 X의 k번째에는 무슨 문자가 오는지 구하여라.
K = int(sys.stdin.readline())
cnt = 0
calc(K)

if cnt%2:
    print(0)
else:
    print(1)
```



## 13305_bkj_주유소

```python
import sys

N = int(sys.stdin.readline())    # N : 도시의 개수
distance = list(map(int,sys.stdin.readline().split()))   # 도시 사이 거리
oil = list(map(int,sys.stdin.readline().split()))        # 주유소의 리터당 가격

# 시작점에서는 무조건 주유
result = distance[0] * oil[0]
minOil = oil[0]
# 1 ~ N-2까지
for i in range(1,N-1):  
    # 이번 도시 기름 싸면, 최소 기준 바꾸기 >> 여기가 최저가격이면 모두 주유하는 결과
    if oil[i] < minOil:
        minOil = oil[i]
        
    result += distance[i] * minOil
print(result)

############# 이거 왜안돼..? ###########
def compute(idx,money):
    global minV

    if idx ==  N-1:
        minV = min(minV,money)
        return
       
    if money > minV:
        return

    # 현재 위치가 가장 기름 싼 위치면
    if oil[idx] == min(oil[idx:]):
        # 여기서 끝까지 갈 기름 주유하기
        compute(N-1,money+sum(distance[idx:])*oil[idx])
    else:
        tmp  = idx+1
        # 기름값 더싼 도시 나올때까지 
        while tmp < N-1 and oil[idx] <= oil[tmp]:
            tmp += 1 
        # 기름 더 싼 도시까지 갈만큼 기름 주유해서 이동
        compute(tmp,money+sum(distance[idx:tmp])*oil[idx])
    

import sys

N = int(sys.stdin.readline())    # N : 도시의 개수
distance = list(map(int,sys.stdin.readline().split()))   # 도시 사이 거리
oil = list(map(int,sys.stdin.readline().split()))        # 주유소의 리터당 가격
oil.pop()

minV = 1000000001 # 제일 왼쪽 도시부터 오른쪽 도시까지 최대 거리보다 큰 값으로 초기화
compute(0,0)
print(minV)
```

