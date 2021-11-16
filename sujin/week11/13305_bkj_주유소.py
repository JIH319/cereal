# 1km마다 1리터의 기름을 사용
# 각 도시에는 단 하나의 주유소
# 도시 마다 주유소의 리터당 가격은 다를 수 있다. 

# def calc(idx,amount,amountsum, money):
#     '''
#     idx: 기름 주유 고민할 위치, 가고자하는 곳
#     amount : 잔여 기름 (다음 도시까지 갈 수 있을지 점검)
#     amountsum : 주유 기름 총합 (현재까지의 주유량으로 도착 도시까지 갈 수 있는지 점검)
#     money: 주유 값
#     '''
#     global minV

#     # 도착
#     if idx == N-1: 
#         minV = min(money,minV)
#         return

#     # 지금 주유된 기름양으로 도착가능 
#     if amountsum >= final:
#         minV = min(money,minV)

#     # 최소값 넘어섬 >> 계산할 필요X
#     if money >= minV: return 

#     # idx : 가고자하는 위치
#     # 도시 사이 거리 <= amount <= 지금부터 도착점까지 거리
#     # 다음 도시까지 못가면 무조건 주유
#     if distance[idx] > amount:
#         for i in range(distance[idx]-amount,final-amount+1):
#             calc(idx+1,amount+i-distance[idx],amountsum+i,money+oil[idx]*i)
#     # 도착점까지 갈수 있는 주유량까지 
#     # 다음 도시까지 갈 수 있음
#     else:
#         for i in range(final-amount+1):
#             calc(idx+1,amount+i-distance[idx],amountsum+i,money+oil[idx]*i)


# def compute(idx,money):
#     global minV

#     if idx ==  N-1:
#         minV = min(minV,money)
#         return
    
#     # 사실 이거 필요없을것같은데....음...
#     if money > minV:
#         return

#     # 현재 위치가 가장 기름 싼 위치면
#     if oil[idx] == min(oil[idx:]):
#         # 여기서 끝까지 갈 기름 주유하기
#         compute(N-1,money+sum(distance[idx:])*oil[idx])
#     else:
#         tmp  = idx+1
#         # 기름값 더싼 도시 나올때까지 
#         while tmp < N-1 and oil[idx] <= oil[tmp]:
#             tmp += 1 
#         # 기름 더 싼 도시까지 갈만큼 기름 주유해서 이동
#         compute(tmp,money+sum(distance[idx:tmp])*oil[idx])
    

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