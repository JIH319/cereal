open = {'(','['}
close = {')',']'}
# 괄호들의 균형이 잘 맞춰져 있는지 판단
while True:
    data = input()
    # 점 하나만 입력들어오면 >> 입력 종료
    if data == '.':
        break
    
    N = len(data)
    # 여는 괄호를 담을 스택
    stack = []
    result = 1 # 1이면 균형잡힌 괄호 >> YES! 0이면 NO! 출력
    for i in range(N):
        # 여는 괄호면,
        if data[i] in open:
            stack.append(data[i])
        # 닫는 괄호면,
        elif data[i] in close:
            # 스택안에 뽑을게 있다면 >> 진행, 그렇지 않다면 반복종료 >> no
            if stack:
                tmp = stack.pop()
                # 괄호쌍 비교 >> 쌍이 맞다면 다음 비교로 이동
                if data[i] == ')' and tmp == '(':
                    continue
                elif data[i] == ']'and tmp == '[':
                    continue
                # 비교결과 쌍이 맞지 않는다 >> 반복종료 >> no
                result = 0
                break
            else:
                result = 0
                break
    # 스택에 여는 괄호가 남아있다면 >> 균형 X >> no
    if stack:
        result = 0
    if result:
        print('yes')
    else:
        print('no')