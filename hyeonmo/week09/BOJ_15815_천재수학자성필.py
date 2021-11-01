# 0~9 숫자와 연산자 + - * / 로만 이루어져 있다.
# 잘못된 수식이 입력되는 경우는 없다.

# 주어진 연산자 목록을 리스트로 만들어 oper 라는 변수에 할당해주고
# input을 받은 data를 하나씩 순회하면서 해당 값이 oper 안에 존재하면 연산자, 아니면 피연산자인 식을 작성한다.
# 연산자일경우 stack의 가장 위의 값이 나중에 작성된 피연산자 이므로 가장 위의 값을 pop하여 b로 그 다음값을 a로 pop 하여 대입한다.
# 나누기 연산자(/)일 경우 3/3일때 1.0이 반환되므로 a//b로 숫자 1이 반환 될 수 있게 몫을 반환하는 식을 작성한다.


# 연산자 리스트 oper
oper = ['+','-','*','/']
data = list(input())

stack = []
for val in data:
    # val이 연산자 라면 stack 상단 2개의 값을 pop
    if val in oper:
        # stack의 최상단 값이 나중에 들어온 값이므로 b,a 로 pop하기
        b = stack.pop()
        a = stack.pop()

        # 연산하여 stack에 다시 push
        if val == '+':
            stack.append(a+b)
        elif val == '-':
            stack.append(a-b)
        elif val == '*':
            stack.append(a*b)
        elif val == '/':
            stack.append(a//b)

    # val이 연산자가 아니라면(피연산자 라면) stack에 push
    else:
        stack.append(int(val))
print(stack[0])
