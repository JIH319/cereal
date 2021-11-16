# 고른 에너지 구슬의 번호를 x라고 한다. 
# 단, 첫 번째와 마지막 에너지 구슬은 고를 수 없다.
# x번째 에너지 구슬을 제거한다.
# Wx-1 × Wx+1의 에너지를 모을 수 있다.
# N을 1 감소시키고, 에너지 구슬을 1번부터 N번까지로 다시 번호를 매긴다. 
'''
4
1 2 3 4
#12

5
100 2 1 3 100
#10400
'''
def calc():
    global maxV
    energy = 0
    for i in range(1,N-1):
        # idx : i번째로 뺄 구슬의 위치
        idx = 0
        for j in range(1,N-1):
            # 순서가 i번째인 구슬의 위치 j 찾기
            if order[j] == i:
                idx = j
                break
        
        # 왼쪽값(val1)  구하기
        tmp = idx-1
        # order가 더 작다 == 이미 먼저 뺀 구슬
        while order[tmp] < order[idx]:
            tmp -= 1
        if tmp == 0:
            val1 = data[0]
        else:
            val1 = data[tmp]
        # 오른쪽값(val2) 구하기
        tmp = idx+1
        while order[tmp] < order[idx]:
            tmp += 1
        if tmp == N-1:
            val2 = data[N-1]
        else:
            val2 = data[tmp]

        energy += val1 * val2
     
    maxV = max(maxV,energy)

# 순열만들기
def perm(idx):

    if idx == N-1:
        # print(order)
        calc()
        return

    for i in range(1,N-1):
        if selected[i] == 0:
            order[idx] = i
            selected[i] = 1
            perm(idx+1)
            selected[i] = 0

N = int(input())
data = list(map(int,input().split()))
# order : 순서 표시할 배열 / index : 구슬 순서, val : 뽑을 구슬 번호
selected = [0] *(N-1) 
order = [987654321]*N
maxV = 0
perm(1)
print(maxV)
