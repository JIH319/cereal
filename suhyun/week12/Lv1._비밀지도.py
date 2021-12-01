# 2진법으로 해당 값을 변경해주는 함수.
def binary(x,y):
    rst = []
    while x-1>-1:
        if y//(2**(x-1)):
            y-=2**(x-1)
            x -=1
            rst.append(1)
        else:
            x -=1
            rst.append(0)
    return rst

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        result = ''
        # 두개의 배열에서 한줄을 가져온뒤에,
        rst1 = binary(n,arr1[i])
        rst2 = binary(n,arr2[i])
        # 하나씩 돌아가면서, 둘다 0 인경우는 공백을, 둘 중 하나라도 1 인경우는 # 을 출력하도록한다.
        for j in range(n):
            if not rst1[j] and not rst2[j]:
                result += ' '
            else:
                result += '#'
        # 그리고 해당 값을 answer 에 append 해준다.
        answer.append(result)
    return answer