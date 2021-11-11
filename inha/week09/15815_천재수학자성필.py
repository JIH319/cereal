import sys
input = sys.stdin.readline().rstrip


# 후위표기법
# 연산자는 +, -, *, /
# 0 으로 나누는 경우, 잘못된 수식이 들어오는 경우는 없음, 계산 중간 값은 모두 정수
# 숫자가 나오면 stack에 push,
# 연산자가 나오면 stack 안의 숫자들 빼서 계산
def postfix(exp):
    stack = []
    for op in exp:
        if op == '+':
            stack.append(stack.pop()+stack.pop())
        elif op == '-':
            val2 = stack.pop()
            val1 = stack.pop()
            stack.append(val1-val2)
        elif op == '*':
            stack.append(stack.pop()*stack.pop())
        elif op == '/':
            val2 = stack.pop()
            val1 = stack.pop()
            stack.append(int(val1/val2))
        else:
            stack.append(op)
    return stack[-1]


exp = list(input())
for i in range(len(exp)):
    # 숫자면 int 타입으로 다시 저장
    if exp[i].isdigit():
        exp[i] = int(exp[i])
print(postfix(exp))



