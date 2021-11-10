# 수평 직선의 왼쪽 방향으로 발사
# 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능

# N: 탑 개수, top : 탑들의 높이를 담는 배열
N = int(input())
top = list(map(int,input().split()))

result = [0] * N    # index: 레이저 출발점, val: 레이저 도착점(왼쪽에서 더 높은 탑의 번호) 
stack = [N-1]       # 현재 비교 기준이 될 (레이저 시작점) 담을 스택
idx = N-2
# 제일 오른쪽에서부터 왼쪽으로 진행
while stack and idx > -1:
    # 더 큰 탑을 발견하면, result에 기록
    while stack and top[stack[-1]] < top[idx]:
        result[stack[-1]] = idx+1   # 탑의 번호는 1~N
        stack.pop()
    
    stack.append(idx)
    idx -= 1
print(' '.join(map(str,result)))