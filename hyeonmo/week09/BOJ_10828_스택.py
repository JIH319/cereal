# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 주어지는 명령의 수 N
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
# 주어지는 정수는 1보다 크거나 같고 100,000보다 작거나 같다.

# for문으로 N번만큼 반복하면서 한번 반복할때마다 input값을 split으로 나눠받아준다.
# 받은 input값을 변수 data 할당하고 data의 첫번째 값이 명령어 이므로 val 변수에 명령어만 따로 할당하여 작성한다.
# 그냥 input을 쓰면 input값이 많아 시간제한 초과가 나니 sys 모듈을 import해서 받아주면 해결된다.


# 시간초과로 인해 sys 활용
import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    data = sys.stdin.readline().split()
    # data의 첫번째 값이 명령어
    val = data[0]

    # 정수 push
    if val == 'push':
        stack.append(int(data[1]))

    # stack이 빈값이면 -1 출력, 아니면 pop한 값을 출력
    elif val == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    # 현재 stack의 개수 출력
    elif val == 'size':
        print(len(stack))

    # stack이 비어있으면 1 아니면 0 출력
    elif val == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    # stack이 비어있으면 -1 출력 아니면 stack의 마지막값 출력
    elif val == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
