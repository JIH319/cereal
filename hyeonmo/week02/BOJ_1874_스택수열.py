N = int(input())
arr = [int(input()) for _ in range(N)] # N만큼 input값 받아서 list에 넣기
i = 0
stack = []
result = []
for val in range(1,N+1): # 1부터 N까지 한개씩
    stack.append(val) # push
    result.append('+')  # push하면 result에 +를 push
    # 마지막에 stack이 다 빈상태로 while을 한번더 검사하는데 빈상태에서 [-1]을 해버려서 인덱스 에러가 난다.
    # stack에 값이 존재할때 검사하라는 조건을 넣어서 인덱스 에러를 피해준다.
    while stack and stack[-1] == arr[i]: # 반복문 검사
        stack.pop() # stack에 값이 있고 stack 마지막인덱스가 arr의 i번째 인덱스와 같은값이면 pop
        result.append('-') # pop 할때마다 -를 result에 push
        i += 1
if stack:
    print('NO') # 반복문이 끝나고 stack에 남은 값이 있다면 NO
else:
    for x in result: # stack이 다 비었다면 result에 있는 값을 출력
        print(x)

