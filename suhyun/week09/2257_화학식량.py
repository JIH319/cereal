# 2257. 화학 식량
cemical = { "H" : 1, "C" : 12, "O" : 16 }

from collections import deque
stack = deque()
s = input()
for k in s:
    if k in cemical:
        stack.append(cemical[k])
    elif k == '(':
        stack.append(k)
    elif k == ')':
        tmp = 0
        while True:
            v = stack.pop()
            if v=='(':
                break
            tmp += v
        if tmp ==0:
            continue
        else:
            stack.append(tmp)
    else: # 숫자일 경우
        tmp = stack.pop()
        tmp = tmp*int(k)
        stack.append(tmp)
print(sum(stack))



