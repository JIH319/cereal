#  연산자가 피연산자 뒤에 위치
# 후순위계산식 결과값 찾기

data = input()
N = len(data)
# 계산과정에서 피연산자를 담을 스택
stack = [0] * N
top = -1
for i in range(N):
    # 피연산자면
    if '0' <= data[i] <= '9':
        top += 1
        stack[top] = int(data[i])
    # 연산자면 >> 계산수행 >> 결과 다시 스택에
    else:
        val2 = stack[top]
        top -= 1
        val1 = stack[top]

        if data[i] == '+':
            stack[top] = val1 + val2
        elif data[i] == '-':
            stack[top] = val1 - val2
        elif data[i] == '*':
            stack[top] = val1 * val2
        elif data[i] == '/':
            stack[top] = val1 / val2
print(int(stack[0]))
