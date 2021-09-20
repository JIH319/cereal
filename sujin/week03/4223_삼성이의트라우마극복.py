   
def ptsd(temp):
    
    if len(temp) < 7 or temp.count('S') < 2 or temp.count('A') < 1 or temp.count('M') < 1 or temp.count('U') < 1 or temp.count('N') < 1 or temp.count('G') < 1:
        return 0
    return 1
    
T = int(input())
for tc in range(1,T+1):
    N = int(input())        # 심사위원 수
    data = []
    datacheck = []
    for i in range(N):
        length = int(input())
        name = input().split()
        datacheck += name
        score = int(input())
        data.append([score,name])
    # 심사위원 이름 안에서 삼성 만들수있는지 없는지 체크
    datacheck = ptsd(datacheck)
    result = 1001*N
    j = 1
    #  powerset
    while datacheck and j < 2**N:
        temp = []
        temp_sum = 0
        for k in range(N):
            # 리스트에 포함 할 말
            if j & (1 << k) != 0:
                temp += data[k][1]  # 이름
                temp_sum += data[k][0]  # 점수
        j += 1
        # 현재 삼성 만들 수 있는 조합의 최소합보다 커지면 그냥 이 조합 계산도 하지말기
        if temp_sum >= result:
            continue
        # 삼성 글자 만들수 없다면,
        if not ptsd(temp):
            continue
        # 삼성 글자 만들 수 있다면,
        else:
            
            result = temp_sum
    
    # 삼성글자 만들 수 있을 때 result : 최소합
    if result != 1001*N:
        print('#{} {}'.format(tc,result))
    else:
        print('#{} {}'.format(tc,-1))                
