"""
stack은 가장 밑에 잇는 애가 크고 그 위로 갈수록 숫자가 작아진다! 상자쌓듯이~~
이 부분을 생각하고 코드를 보면 이해하기 쉽다~!
"""
N = int(input())
arr = [int(input()) for _ in range(N)]

stack = []
cnt = 0
# for문으로 건물들 순서대로 확인!
for i in range(N-1):
    # 현재 건물 높이(idx)와 다음 건물 높이(idx+1)를 비교
    if arr[i] > arr[i+1]:
        # 앞의 건물이 다음 건물보다 더 클 경우, stack에 현재 건물의 높이를 넣고 스택 갯수만큼 cnt + 해준다
        # 왜냐하면, stack 가장 위에 있는 애가 밑에 애들보다 숫자가 낮기 때문에 무조건 밑의 건물 애들도 다음 건물 높이보다 높을것!
        stack.append(arr[i])
        cnt += len(stack)
        # 다음 건물이 더 높을 경우,
    else:
        # stack에 잇던 건물을 하나씩 꺼내서, 다음건물과 높이 비교하기~
        while stack:
            if stack[-1] > arr[i+1]:
                cnt += len(stack)
                break
            # 다음건물보다 stack 건물이 더 낮다 ㅠㅠ 졌으면 pop (사라짐)
            else:
                stack.pop()

print(cnt)
