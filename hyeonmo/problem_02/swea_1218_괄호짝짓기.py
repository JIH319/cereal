for tc in range(1,11):
    N = int(input())
    input_val = input()
    stack = []
    left = ['(','[','{','<']    # 왼쪽 괄호 리스트
    right = [')',']','}','>']   # 오른쪽 괄호 리스트
    result = 1  # 결과값 1로 미리 지정
    for val in input_val:   # input 값을 for반복으로 하나씩 검사
        if val in left:     # left 안에 있다면 stack 에 push
            stack.append(val)
        elif val in right:  # right 안에 있다면
            if right.index(val) == left.index(stack[-1]):   # val이 stack의 마지막값과 짝이 맞는지 검사
                stack.pop() # 맞으면 스택의 마지막 값 pop 하고 val은 아무런 지정을 안해줌
            else:
                result = 0  # 안맞으면 유효하지 않은 값이라 0으로 지정하고 반복문 종료
                break
    
    print('#{} {}'.format(tc,result))