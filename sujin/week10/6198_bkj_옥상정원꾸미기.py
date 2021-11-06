# 모든 빌딩은 일렬로 서 있고 오른쪽으로만 볼 수 있다
# 자신이 위치한 빌딩보다 높거나 같은 빌딩이 있으면 
# 그 다음에 있는 모든 빌딩의 옥상은 보지 못한다

N = int(input())    # N : 빌딩의 개수
buildings = [0] * N # building : 빌딩 높이를 담는 배열
for i in range(N):
    buildings[i] = int(input())

buildings.append(1000000000) # 빌딩최대 높이 마지막에 추가
result = [0] * N    # index : 빌딩번호, value : 옥상 볼 수 있는 빌딩 개수
stack = [0]  # val : 빌딩번호(인덱스)
idx = 1
while stack and idx < N+1:
    
    # buildings[stack[-1]] : 현재 스택 마지막 빌딩의 높이
    # 같거나 더 높은 빌딩 나오면 >> 결과 배열 값 계산
    while stack and buildings[stack[-1]] <= buildings[idx]:
        result[stack[-1]] = idx - stack[-1] - 1
        stack.pop()
    
    # 더 작은 빌딩부터 계산
    stack.append(idx)
    idx += 1
    
# print(result)
print(sum(result))

'''
# 시간초과ver

result = [0]*N
for i in range(N-1):
    count = 0
    for j in range(i+1,N):
        if buildings[i] <= buildings[j]:
            break
        count += 1
    result[i] = count
print(sum(result))
'''