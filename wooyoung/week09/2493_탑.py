N = int(input())
arr = list(map(int, input().split()))
stack = []
result = [0 for _ in range(N)]
# 오른쪽에서 왼쪽으로 순서대로 건물들을 확인!
for i in range(-1,-N,-1):
    # 현재 건물 < 다음 건물 높이라면, 높은 건물로 result에 넣는다.
    if arr[i] < arr[i-1]:
        result[i] = N+i
        # 만약 stack이 채워져 있다면, 다음 건물 높이와 비교해서 다음 건물이 높은 경우 result에 넣어주고 pop()
        while stack:
            if arr[stack[-1]] < arr[i-1]:
                result[stack[-1]] = N+i
                stack.pop()
            # 만약 stack[-1] 높이가 다음 건물보다 높은 경우 break해서 for반복문 idx + 1 해준다.
            else:
                break
    # 현재 건물 > 다음 건물 높이라면, 아직 자신보다 높은 건물을 만나지 못한 것이기 때문에 다음 for 반복문을 노린다.
    else:
        stack.append(i)

for i in range(N):
    print(result[i], end=" ")