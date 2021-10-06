T = int(input())
for tc in range(1, T+1):
    number = input()
    data = {'01': '31', '02': '28', '03': '31', '04': '30', '05': '31', '06': '30',
            '07': '31', '08': '31', '09': '30', '10': '31', '11': '30', '12': '31'}
    

    # 연,월,일 로 슬라이싱
    year, month, day = number[:4], number[4:6], number[6:8]

    if '01' <= month <= '12' and '01' <= day <= data.get(month):
        print('#{} {}/{}/{}'.format(tc, year, month, day))
    else:
        print('#{} {}'.format(tc, -1))
