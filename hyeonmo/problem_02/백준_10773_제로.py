K = int(input())
stack = []
for _ in range(K):
    N = int(input())
    if N == 0:
        stack.pop() # N이 0이면 pop
    else:
        stack.append(N) # 0이 아니면 push
if not stack:   # 다 끝난후에 stack이 비었으면 0
    print(0)
else:
    print(sum(stack))   # 남아있으면 합해서 출력
