# 10773 제로!
# 나코더 기장 재민이는 동아리 회식을 준비하기 위해 장부를 관리하는 중.
# 재현이는 재민이를 돕는다. 재현이는 돈을 시수로 잘못 부르는 사고를 치기 일수.
# 재현이는 잘못된 수를 부를 떄 마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지운다.

# 스택을 활용하자!
from collections import deque
stack = deque()
# [ 입력 ]
# 첫 번째 줄에 정수 K 가 주어진다.
K = int(input())
# 스택
# 이후 K개의 줄에 정수 1개씩 주어진다.
for _ in range(K):
    n = int(input())
    # n 이 존재할경우 stack 에 append 해준다.
    if n:
        stack.append(n)
    # 존재하지 않을경우, 가장 최근에 들어간 수를 pop 해준다.
    else:
        stack.pop()
# 최종적으로 나온 stack 에 sum 을 활용한다.
print(sum(stack))
