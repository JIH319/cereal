# 오렐리는 슈퍼개발자래.. .멋지다.. 완전 쩔어
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수/ 스테이지에 도달한 플레이어 수

def solution(N, stages):
    rst = {}
    # 총 도전하는 유저의 수
    users = len(stages)
    # 1 스테이지 부터 시작하므로, 범위는 1~ N 까지
    for s in range(1,N+1):
        # 유저가 있는 동안에는, 딕셔너리로 key 는 stage, value는 실패율로 넣어주자.
        if users != 0:
            rst[s] = stages.count(s)/users
            users -= stages.count(s)
        else:
             rst[s] = 0
    # 함수 출력, rst 의 key를 rst value 의 내림차순으로 정렬해준다.
    answer = sorted(rst.keys(),key=lambda x: rst[x],reverse=True)
    return answer
