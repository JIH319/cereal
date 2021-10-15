def check(month, day):
    # 유효한 월, 일인지 확인
    # 문자열을 정수타입으로 변환
    month = int(month)
    day = int(day)
    result = False
    # 경우를 나눠서 비교
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= day <= 31:
            result = True
    elif month in [4, 6, 9, 11]:
        if 1 <= day <= 30:
            result = True
    elif month == 2:
        if 1 <= day <= 28:
            result = True
    # 유효하면 result는 True, 유효하지 않으면 result는 False 반환
    return result


T = int(input())

for tc in range(1, T+1):
    nums = input() # 문자열로 그대로 받아옴
    # 년, 월, 일 슬라이싱으로 자름
    y = nums[0:4]
    m = nums[4:6]
    d = nums[6:8]

    if check(m, d): # 유효한 연월일이면
        print('#{} {}/{}/{}'.format(tc, y, m, d))
    else:
        print('#{} {}'.format(tc, -1))




