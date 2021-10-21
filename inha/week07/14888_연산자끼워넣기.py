import sys
input = sys.stdin.readline


def cal(op):    # op : 순열이 완성된 연산자 리스트
    n = nums[:] # 숫자 num를 복사
    for i in range(N-1): # 연산자 수 만큼 for문
        if op[i] == 0:
            # 숫자 리스트 n의 i번째와 i+1번째를 i번째 연산자로 계산
            n[i+1] = n[i] + n[i+1]
        elif op[i] == 1:
            n[i+1] = n[i] - n[i+1]
        elif op[i] == 2:
            n[i+1] = n[i] * n[i+1]
        elif op[i] == 3:
            if n[i] < 0:
                n[i+1] = - ((-n[i]) // n[i+1])
            else:
                n[i+1] = n[i] // n[i+1]
    return n[-1]


# 연산자들의 순열을 만들고
# 완성된 순열을 가지고 계산하기
def perm(k):
    global min_v, max_v
    # 순열이 숫자의 개수인 N보다 1작은 N-1이 되었을 때 return
    if k == N-1:
        # 순열이 완성되었으므로 계산
        ans = cal(perm_lst)
        if ans < min_v:
            min_v = ans
        if ans > max_v:
            max_v = ans
        return
    # 순열이 덜 완성되었다면
    else:
        # 연산자가 저장된 리스트를 돌면서
        for i in range(4):
            # operators의 i번째에 추가될 연산자가 있다면
            if operators[i]:
                # 연산자를 의미하는 인덱스 i를 perm_lst에 추가
                perm_lst.append(i)
                # i번째 인덱스가 한개 사용되었으므로 -1 해줌
                operators[i] -= 1
                # 순열의 다음번째에 올 연산자를 구하기 위해 재귀호출
                perm(k+1)
                # i번째 인덱스가 다 사용되었으므로 다시 +1
                operators[i] += 1
                # perm_lst도 원상복귀
                perm_lst.pop()


N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
# 완성된 연사자들의 순열을 저장할 리스트
perm_lst = []
min_v, max_v = 1000000000, -1000000000
perm(0)
print(max_v, min_v, sep='\n')
