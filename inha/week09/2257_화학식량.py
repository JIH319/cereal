# 음.. 이 방법은 stack이 아닌 것 같긴 한데..
import sys
input = sys.stdin.readline

chemical = list(input().rstrip())

# 각 원자의 질량
dic_vol = {'H': 1, 'C': 12, 'O': 16}
# 원자는 9개까지 가능
nums = {'2', '3', '4', '5', '6', '7', '8', '9'}
N = len(chemical)

# 괄호 안의 값들끼리 계산하기 위해서
# 괄호의 계산값은 각 인덱스에 저장됨
# H(CO) 일 경우 lst[0] = 1(H),
# lst[1] = 28(CO) 가 저장되도록
lst = [0]*N

# idx: 화학식을 입력받은 chemical 리스트에 접근하기 위한 인덱스 변수
# i: 합계를 저장할 lst의 인덱스 변수
# val_cur: 계산 중간에 원자 개수와 원자량을 계산하기 위한 현재 값 변수
idx, i, cur_val = 0, 0, 0
# 입력받은 리트스를 끝까지 돈다.
while idx < N:
    # chemical[idx]가 원자이면(H, C, O)
    # 현재 값 cur_val 변수에 원자량 저장하고
    # lst[i]에 해당 원자량 값을 더한다.
    if chemical[idx] == 'H' or chemical[idx] == 'C' or chemical[idx] == 'O':
        cur_val = dic_vol[chemical[idx]]
        lst[i] += dic_vol[chemical[idx]]
    # chemical[idx]값이 nums안에 들어있는 숫자라면
    # 원자 다음에 숫자가 올 것이므로 앞에서 lst[i]에 해당 원자량만큼 더해준 것을 빼주고
    # 해당 원자량(cur_val)과 현재 idx가 가르키는 숫자를 곱한 값을 다시 더해준다.
    elif chemical[idx] in nums:
        lst[i] -= cur_val
        lst[i] += cur_val * int(chemical[idx])
    # 열린 괄호가 오면 괄호 안의 값은 따로 계산되어야 하므로
    # lst의 인덱스인 i를 +1 증가시켜 lst[i+1]에서 새로오는 괄호 안의 값들을 계산하여 저장하도록 함
    elif chemical[idx] == '(':
        i += 1
    # 닫힌 괄호가 오면 현재 괄호에서 계산된 값(lst[i])값을 현재 값(cur_val)로 저장해주고
    # lst[i-1] 값과 cur_val를 더해서 lst[i-1]에 저장해준다.
    # lst[i]는 0으로 초기화 시킨다.(다음 새로운 괄호가 나오면 해당 인덱스번째가 사용되어야 하므로)
    elif chemical[idx] == ')':
        cur_val = lst[i]
        lst[i] = 0
        i -= 1
        lst[i] += cur_val
    # 조건문이 모두 끝나면 다음 식의 요소를 판단하기 위해 idx +1 증가
    idx += 1

# while문이 모두 끝나면 각 괄호의 값을 저장한 lst의 합을 구한다.
print(sum(lst))

