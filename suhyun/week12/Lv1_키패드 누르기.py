# 절대 값을 구해주는 사용자 정의 함수
def absolute(n):
    if n>0:
        return n
    else:
        return -n

def solution(numbers, hand):
    answer = ''
    # 우선 생각해보자. [1,4,7] 은 왼손, [3,6,9] 는 오른손, [2,5,8,0]은 거리에 따라, 같을 경우 hand 를 따른다.
    # 그렇다면 눌렀을떄의 위치도 저장하여, [2,5,8,0] 일 때의 거리도 알아야 겠네!
    # [2,5,8,0] 에 이미 위치해있을 경우도, 거리로 계산해야하네! , 그러다 [1,4,7], [3,6,9] 위치로 갈떄는 다시 이동!
    # 왼손 현재 위치 *
    lc = [3,0]
    # 오른손 현재 위치 #
    rc = [3,2]
    for number in numbers:
        # 왼손 하나로 뭉쳐주기!
        if number%3==1 and number!=0:
            lc = [number//3,0]
            answer +='L'
        # 오른손 하나로 뭉쳐주기!
        elif number%3==0 and number!=0:
            rc = [number//3-1,2]
            answer += 'R'
        # 중간인 경우도 뭉쳐주자
        elif number%3 == 2:
            if absolute(lc[0]-number//3)+absolute(lc[1]-1)>absolute(rc[0]-number//3)+absolute(rc[1]-1):
                rc = [number//3,1]
                answer += 'R'
            elif absolute(lc[0]-number//3)+absolute(lc[1]-1)==absolute(rc[0]-number//3)+absolute(rc[1]-1):
                if hand == 'left':
                    lc = [number//3,1]
                    answer += 'L'
                else:
                    rc = [number//3,1]
                    answer += 'R'
            else:
                lc = [number//3,1]
                answer +='L'
        # 0 인 경우는 특이하니까 빼주자.
        elif number == 0:
            if absolute(lc[0]-3)+absolute(lc[1]-1)>absolute(rc[0]-3)+absolute(rc[1]-1):
                rc = [3,1]
                answer += 'R'
            elif absolute(lc[0]-3)+absolute(lc[1]-1)==absolute(rc[0]-3)+absolute(rc[1]-1):
                if hand == 'left':
                    lc = [3,1]
                    answer += 'L'
                else:
                    rc = [3,1]
                    answer += 'R'
            else:
                lc = [3,1]
                answer +='L'
                                                          
    return answer