'''
10            
6 8 3         
0 0 1 0 1 0 0 1
0 1 0 0 0 1 1 1
0 1 1 1 0 0 0 0
1 1 1 1 0 0 0 1
0 1 1 0 1 0 0 1
1 0 1 0 1 1 0 1
6 8 3         
1 1 1 1 0 0 1 0
0 0 1 1 0 1 0 1
1 1 1 1 0 0 1 0
1 1 1 0 0 1 1 0
1 1 0 1 1 1 1 0
1 1 1 0 0 1 1 0

#1 2
'''
def check():
    # 열별로 기준 충족하는지 체크하는 함수
    # 해당 열 기준 충족 >> 다음 열 >> 마지막열까지 충족하면 1
    for i in range(W):
        cnt = 1
        remember = -1
        for j in range(D):
            if remember == data[j][i]:
                cnt+=1
            else:
                cnt = 1
            # 검증기준 충족하면 다음 열로
            if cnt == K:
                break
            remember = data[j][i]
        # 한 열이라도 기준 미달이면 함수 종료
        if cnt < K:
            return 0
        
        
    # 모든 열 끝까지 검증 체크했으면 return 1
    return 1

def check2(val):
    # 약품 투입후 >> 열별로 기준 충족하는지 체크하는 함수
    # 해당 열 기준 충족 >> 다음 열 >> 마지막열까지 충족하면 is_break값을 val로
    # val : 약품 투입할 행 개수
    # selected : 고를 행 체크할 리스트
    # put : 고른 행에 어떤 약품을 넣을지 표시한 리스트

    global is_break
    # print(selected)
    # print(put)
    for i in range(W): # 열고르기
        cnt = 1
        pidx = 0
        remember = -1
        for j in range(D): # 해당 열, 한행씩 위에서부터 아래로
            # 해당 행이 선택된 행이면 
            if selected[j]: 
                # 이전 값과 put(약품 표시)와 비교
                # print(j,pidx)
                if remember == put[pidx]:
                    cnt += 1
                    remember = put[pidx]
                    pidx += 1
                else:
                    cnt = 1
                    remember = put[pidx]
                # 현재 값 저장 >>  다음 비교를 위해
                
            # 선택된 행 아니면 그냥 원래값으로 비교
            else:
                if remember == data[j][i]:
                    cnt+=1
                else:
                    cnt = 1 
                # 현재 값 저장 >>  다음 비교를 위해
                remember = data[j][i]
            # 검증기준 충족하면 다음 열로
            if cnt == K:
                break
             
        # 한 열이라도 기준 미달이면 함수 종료
        if cnt < K:
            return 
        # print(i,'열은 통과')
    # 모든 열 끝까지 검증 체크했으면 return 1
    is_break = val
    return 

def comb(idx,cnt,num):
    '''
    약품을 투입할 행을 고를 함수
    idx : 현재 포함 여부 선택할 행
    cnt : 포함한 행 개수 표시
    num : 고를 행 개수 1 <= num <= K
    '''

    # 열 다 골랐으면
    if cnt == num:
        # print(selected)
        comb2(0,num)

        # 이미 해당 선택 개수에서 답 나왔음 >> 종료
        if is_break:
            return     
        
    # 골라야할 행 개수 덜 골랐으면 return
    if idx == D:
        return  

    for i in range(2):
        selected[idx] = i
        comb(idx+1,cnt+i,num)
        if is_break:
            return 
        selected[idx] = 0 # 초기화

def comb2(idx,val):
    # A약품 넣을지 B약품 넣을지 행별로 중복순열로 나타낼 함수
    # val : 약품 투입할 행 개수
    global is_break

    if idx == val:
        check2(val)
        return
        
    for i in range(2):
        put[idx] = i
        comb2(idx+1,val)
        if is_break:
            return 



for tc in range(1, int(input())+1):
    # D : 보호필름 두께 , W : 보호필름 너비 , K : 합격기준
    D, W, K = map(int, input().split())
    # A : 0, B : 1
    data = [list(map(int, input().split())) for _ in range(D)]

    # 성능검사를 통과할 수 있는 약품의 최소 투입 횟수
    # 약품을 투입하지 않고도 성능검사를 통과하는 경우에는 0을 출력
    is_break = 0
    result = check()
    if result:
        print('#{} {}'.format(tc, 0))
    else:
        # 약품 투입이 필요하다면 >> 투입할 행 고르기
        # i : 투입할 행 개수, 투입 행 최대 개수는 K
        for i in range(1,K):
            # 고를 행 체크할 리스트
            selected = [0] * D
            # 어떤 약품 넣을지 표시할 리스트(A약품은 0, B약품은 1)
            put = [0]*i
            comb(0,0,i) # 약품을 투입할 행을 고를 함수
            
            if is_break:
                break
    
        if is_break:
            print('#{} {}'.format(tc,is_break))
        else:
            print('#{} {}'.format(tc,K))
        
        