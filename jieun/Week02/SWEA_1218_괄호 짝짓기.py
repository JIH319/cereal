from collections import deque
exp = {'[':']', '{':'}', '(':')', '<':'>'}
for tc in range(1, 11):
    answer = 1
    _ = int(input())
    q = deque()
    gwal = input()
    for g in gwal:
        if g in exp.keys():
            q.append(g)
        else :
            if exp[q[-1]] == g :
                q.pop()
            else:
                answer = 0
                break

    print('#{} {}'.format(tc, answer))