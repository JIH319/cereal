# 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수
N,M = map(int,(input().split()))
data = list(map(int,input().split()))

tmp = 0 # M <= tmp 될때까지 누적합 담을 변수
cnt = 0 # tmp == M 가 되면 + 1 : M 이 되는 경우의 수 
sidx = 0 # 탐색 누적합 시작 인덱스
idx = 0 # data 탐색 인덱스

while idx < N:
    tmp += data[idx]
    if tmp >= M:
        # 수열의 합이 M
        if tmp == M:
            cnt += 1          
        # tmp >= M 일때,
        # # 누적합 변수 초기화, 경우의 수 +1, 
        # 누적합 시작인덱스 다음부터 다시 탐색   
        tmp = 0
        sidx = sidx + 1
        idx = sidx
        continue 
    idx += 1 

print(cnt)    
