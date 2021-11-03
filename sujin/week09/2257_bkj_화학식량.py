# 화학식은 H, C, O, (, ), 2, 3, 4, 5, 6, 7, 8, 9만으로 이루어진 문자열
# H : 1, C : 12, O : 16
HCO = {'H':1,'C':12,'O':16}
HCO_keys = {'H','C','O'}

data = input()
N = len(data)

idx = 0
stack = []
while idx < N:
    # 여는 괄호 나올때마다 현재까지의 tmp stack에 담고 >> tmp 초기화

    # 화학원자
    if data[idx] in HCO_keys:
        stack.append(HCO[data[idx]]) 
    # 여는 괄호
    elif data[idx] == '(':
        stack.append(data[idx])
        pass
    # 닫는 괄호
    elif data[idx] == ')':
        tmp = 0
        # 여는 괄호 나올때까지 더해서 stack에 담아주기
        while stack[-1] != '(':
            tmp += stack.pop()
        stack.pop() # 여는 괄호 빼기
        stack.append(tmp) # 방금 괄호쌍 안의 합 넣어주기
        tmp = 0

    # 숫자 >> 직전이 화학원자 or 괄호
    elif '2' <= data[idx] <= '9':
        stack[-1] = stack[-1] * int(data[idx])

    idx += 1
    # print(stack)
print(sum(stack))
'''
# result : 덩어리씩 담을 리스트
# tmp : 계산이전 임시 누적문자
result = []
idx = 0
while idx < N:
    # 여는 괄호 나오면
    if data[idx] == '(':
        stack = ['(']
        tmp = 0
        while stack:
            # 닫는 괄호 >> 하나의 괄호쌍 처리하기!
            if data[idx] == ')':
                # 여는 괄호 나올때까지
                while stack[-1] != '(':
                    val = stack.pop()
                    # 숫자 
                    if '2' <= val <= '9':
                        tmp += HCO[stack.pop()] * (int(val)-1)
                    # 화학원자
                    else:
                        tmp += HCO[val]
                
                stack.pop() # 여는 괄호 빼기
                result += tmp
                remember = tmp
                
            # 숫자가 나오면
            elif '2' <= data[idx] <= '9':
                result += remember * (int(data[idx])-1)
            # 문자가 나오면
            elif data[idx] in HCO.keys():
                stack.append(data[idx])
            idx += 1


print(result)
    

'''


