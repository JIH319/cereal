'''
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
'''
# k(k>6)개의 수를 골라 집합 S를 만든 다음 그 수만 가지고 번호를 선택
# 첫 번째 수는 k (6 < k < 13)이고, 
# 다음 k개 수는 집합 S에 포함되는 수이다. 
# S의 원소는 오름차순으로 주어진다.
# 입력의 마지막 줄에는 0이 하나 주어진다. 
# 사전 순으로 출력/ 테케 한줄 비우기

def comb(idx, cnt):
    '''
    idx : 현재 고를지말지 정할 인덱스
    cnt : 현재 고른 숫자의 개수 (6 될때까지 함수 재귀호출)
    '''
    # 6개 골랐으면 출력
    if cnt == 6:
        for i in range(N):
            if selected[i]:
                print(data[i],end=' ')
        print()
        return

    # 인덱스끝까지 왔으면 더이상 X
    if idx == N:
        return

    # 사전순 출력을 위해 일단 선택(1) > (0)
    for i in range(1,-1,-1):
        selected[idx] = i
        comb(idx+1,cnt+i)
        selected[idx] = 0
    pass

while True:
    data = list(map(int,input().split()))
    N = int(data.pop(0))
    # input 0 들어올때까지 반복
    if N == 0:
        break
    # selected : 선택 표시
    selected = [0]*N
    comb(0,0)
    print()

