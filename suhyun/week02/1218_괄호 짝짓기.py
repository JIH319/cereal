# 1218. [S/W 문제해결 기본] 4일차 - 괄호 짝짓기

# 4 종류의 괄호 문자들 '()','[]','{}','<>'로 이루어진 문자열ㅇ 주어진다.
# 괄호의 짝이 모두 맞는지 판별하는 프로그램을 작성한다

# deque 를 활용하자
from collections import deque


# 테스트 케이스가 유효한지 안유호한지 확인할 confirm 함수 생성
def confirm(t, n):
    # 값을 받을 que 생성
    stack = deque()
    # 테스트 케이스 줄 길이 만큼 반복문 생성
    for i in range(n):
        # 여는 괄호일경우 바로 append 해준다.
        if t[i] == '{' or t[i] == '[' or t[i] == '(' or t[i] == '<':
            stack.append(t[i])
        # 닫는 괄호일겨우, 스택에 저장된 마지막 값이 매칭 될 경우, continue 로 올려주고,
        # 안될 경우 return 0 을 바로 반환한다.
        elif t[i] == ')':
            if stack.pop() == '(':
                continue
            else:
                return 0
        elif t[i] == '}':
            if stack.pop() == '{':
                continue
            else:
                return 0
        elif t[i] == ']':
            if stack.pop() == '[':
                continue
            else:
                return 0
        elif t[i] == '>':
            if stack.pop() == '<':
                continue
            else:
                return 0
    # 반복문이 끝나도록 반환이 되지 않을 경우, 모두 매칭이 된 경우 1을 반환한다.
    return 1


# [ 입력 ]
T = 10
for tc in range(1, T + 1):
    # 각 테스트 케이스의 첫 번째 줄에는 테스트케이스의 길이가 주어진다.
    N = int(input())
    # 괄호 짝짓기 테스트 케이스가 주어진다.
    test = input()
    # 결과 값 1 과 0을 반활 받을 result 변수 생성
    result = confirm(test, N)
    # 결과 값 출력
    print('#{} {}'.format(tc, result))
