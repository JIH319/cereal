# H : 수소, 질량 1
# C : 탄소, 질량 12
# O : 산소, 질량 16

# 입력값을 숫자로 변환하여 stack에 넣고
# 입력값이 숫자라면 stack의 마지막요소랑 곱하기
# 입력값이 닫는 괄호라면 여는 괄호가 나올때까지 숫자를 꺼내서 더해주기

data = list(input())
stack =[]

for i in data:
    if i == 'H':
        stack.append(1)
    elif i =='C':
        stack.append(12)
    elif i =='O':
        stack.append(16)
    elif i == '(':
        stack.append(i)
    elif i == ')':
        # 여는 괄호가 나올때까지 더한다.
        sum_val = 0
        while True:
            if stack[-1] != '(':
                pop_data = stack.pop()
                sum_val += pop_data
            # 여는 괄호가 나온다면 여는 괄호 pop해서 빼주고 계속 더한값 sum_val을 push 한다.
            else:
                stack.pop()
                stack.append(sum_val)
                break
    else:
        pop_data = stack.pop()
        stack.append(pop_data*int(i))

print(sum(stack))