import sys
input = sys.stdin.readline

# 괄호검사
# 아무 괄호도 오지 않고 종료(.)될 경우에도 'yes' 출력
# 들어오는 입력을 모두 처리하기 위해 while True
while True:
    sentence = input().rstrip()
    # 입력 종료 조건으로 맨 마지막에 . 이 들어오므로
    # 종료 조건
    if sentence == '.':
        break
    # 열린 괄호를 저장할 stack 생성
    stack = []
    # 괄호가 짝을 이루는지 알려주는 isTrue 변수
    # 짝을 이루면 True, 안 이루면 False
    isTrue = True
    for c in sentence:
        # 열린 괄호가 오면 stack에 넣고
        if c == '(' or c == '[':
            stack.append(c)
        # 닫힌 괄호가 오면 stack에서 pop한 값과 비교하기
        elif c == ')':
            # 닫힌 괄호가 왔을 때 stack이 비어있거나
            # 열린 괄호에 맞는 닫힌 괄호가 아닐 경우
            # 짝이 맞지 않으므로 isTrue 변수에 False를 저장하고 break
            if not stack or stack.pop() != '(':
                isTrue = False
                break
        elif c == ']':
            if not stack or stack.pop() != '[':
                isTrue = False
                break
    # 괄호의 짝이 맞으면 stack 안에 있는 괄호는 모두 pop 되어야함
    # 괄호의 짝이 맞지 않는 경우
    # 1. stack에 남아있다는 것은 괄호 짝이 맞지 않음을 의미
    # 2. stack이 비어있어도 isTrue가 False인 경우는 짝이 맞지 않음
    if stack or not isTrue:
        print('no')
    else:
        print('yes')


