# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값
'''
5
3 1 4 3 2

32
'''

N = int(input())
data = list(map(int,input().split()))
data.sort() # 오름차순 정렬
for i in range(1,N):
    # 누적합
    data[i] = data[i-1] + data[i]
print(sum(data))