# 4299. 태혁이의 사랑은 타이밍 - D 3
# 불쌍한 태혁이 ㅠ..
def Chim(d, h, m):
    Dt = 11  # 어짜피 다 11이니 통일하자
    rst = (d - Dt) * 24 * 60 + (h - Dt) * 60 + (m - Dt)
    if rst < 0:
        return -1
    return rst


# [ 입 력 ]
# 첫째 줄에는 테스트 케이스의 수가 주어진다.
T = int(input())
for tc in range(1, T + 1):
    # 테스트 케이스 각 줄에는 3개의 정수가 주어진다.
    D, H, M = map(int, input().split())

    # 각각의 케이스마다 각 줄에 태혁이가 얼마나 오랫동안 바람을 맞았는지 분 단위로 출력한다
    # 태혁이가 소개팅 약속시간 전에 차였다면 놀리기엔 너무 불쌍하므로 -1을 출력한다.
    # 재혁이의 소개팅 약속 시간 2011년 11월 11일 오전 11시 11분

    # 차인 분 확인하기 위한 함수 불러오기
    result = Chim(D, H, M)
    print('#{} {}'.format(tc, result))
