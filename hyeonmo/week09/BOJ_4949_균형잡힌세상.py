# 주어진 입력값의 괄호가 균형이 잘 맞춰져 있는지 판단하는게 목적이다.
# 입력값은 한 줄일 수도 있고 여러 줄 일 수도 있다.
# 입력의 종료조건으로 맨 마지막에 점 하나(단 하나 ".")가 들어온다.
# 몇줄인지 N이 안주어지기 때문에 종료조건인 점 하나가 올때까지 반복하여 입력값을 받아야 한다.

# 여는 괄호 리스트인 A와 닫는 괄호 리스트인 B를 만들어두자
# 입력받은 데이터를 한 줄 마다 한요소씩 순회하며 검사하자
# 만약 순회하는 i가 여는 괄호 라면 stack에 push 한다.
# 닫는 괄호 라면 stack의 마지막요소를 pop하여 비교한다.
# pop은 빈값에서 실행하면 오류가 발생하고 빈값인 상태에서 닫는 괄호가 나와도 균형이 맞지 않으니 no를 반환
# 검사가 끝난후에 stack에 여는 괄호가 남아있다면 균형이 맞지않음



# 종료조건 설정을 위해 함수로 작성하였다.
def solve(val):
    stack = []
    for i in val:
        # i가 여는괄호 리스트에 있다면 stack에 push
        if i in A:
            stack.append(i)
        # i가 닫는괄호 리스트에 있고 빈값이 아니라면 pop (빈값이면 균형 맞지 않음 no 출력)
        elif i in B:
            if len(stack) == 0:
                return 'no'
            sp = stack.pop()

            # 닫는 괄호인 i가 여는 괄호인 sp와 균형이 맞지 않으면 no 출력 맞으면 pass
            if i == ')' and sp != '(':
                return 'no'

            elif i == ']' and sp != '[':
                return 'no'
    # 반복문이 끝나고 stack이 빈값이 아니면 균형이 맞지 않는 문장
    if len(stack) > 0:
        return 'no'
    else:
        return 'yes'


data = []
while True:
    input_data = input()
    # 점(.)이 나올때 까지 입력값 받기
    if input_data != '.':
        data.append(input_data)
    else:
        break

A = ['(','[']   # 여는 괄호 리스트
B = [')',']']   # 닫는 괄호 리스트
for val in data:# 입력값을 한줄씩 검사
    result = solve(val)
    print(result)