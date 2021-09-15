for i in range(1,11):
    N = int(input())
    data = input()
    stack = []
    opendata = ['<','(','[','{']

    top = -1
    result = 1
    for j in range(N):
        # 여는 괄호일때
        if data[j] in opendata:
            top += 1
            stack.append(data[j]) 
            
        # 닫는 괄호일때
        else:
            if data[j] == '>':
                if stack[top] != '<':
                    result = 0
                    break
                else:
                    top -= 1
                    stack.pop()
            
            if data[j] == ')':
                if stack[top] != '(':
                    result = 0
                    break
                else:
                    top -= 1
                    stack.pop()

            if data[j] == ']':
                if stack[top] != '[':
                    result = 0
                    break
                else:
                    top -= 1
                    stack.pop()

            if data[j] == '}':
                if stack[top] != '{':
                    result = 0
                    break
                else:
                    top -= 1
                    stack.pop()
    print('#{} {}'.format(i,result))