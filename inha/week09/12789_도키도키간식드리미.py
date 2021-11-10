import sys
input = sys.stdin.readline

N = int(input())
# 현재 서있는 줄
line = list(map(int, input().split()))
# stack 구조로 만들어주기 위해 line을 reverse
line.reverse()
# 현재 서 있는 줄에서 옮겨갈 수 있는 대기 줄
waiting = []

# 번호표가 1번 부터 시작하므로
n = 1
# 번호표가 N이 될때까지 while문
while n < N+1:
    # line에 사람이 있고, line의 마지막 번호가 현재 번호(n)라면
    # 그 번호를 pop해서 빼주고 번호표 +1(다음 사람) 해준다.
    if line and line[-1] == n:
        line.pop()
        n += 1
    # line에 사람이 없거나 line의 마지막 번호가 현재 번호(n)가 아니라면 다음으로 waiting에서 찾음
    # waiting에 사람이 있고 현재 번호(n)을 가진 사람이 있다면 pop해주고
    # 번호표(n)을 +1 해줌
    elif waiting and waiting[-1] == n:
        waiting.pop()
        n += 1
    # 위 조건을 만족하진 않지만 (즉, 통로로 나올 수 있는 사람 중에 현재 번호를 가진 사람이 없다면)
    # line의 마지막에 있는 사람을 waiting으로 옮겨준다.
    elif line:
        waiting.append(line.pop())
    # 위 조건을 모두 만족하지 않는다면(즉, line에 사람이 없고 waiting 마지막 번호가 현재번호와 일치하지 않는다면)
    # 이는 순서대로 간식을 받을 수 없다는 뜻이므로 break로 while문을 빠져나옴
    elif waiting:
        break
# line과 waiting 줄이 다 비어야 간식 받을 수 있음
if not line and not waiting:
    print('Nice')
else:
    print('Sad')
