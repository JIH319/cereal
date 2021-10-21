date = {
    '01':31,
    '02':28,
    '03':31,
    '04':30,
    '05':31,
    '06':30,
    '07':31,
    '08':31,
    '09':30,
    '10':31,
    '11':30,
    '12':31,
}

for tc in range(1,int(input())+1):
    data = input()
    month = data[4:6]
    day = data[6:]
    is_true = 0
    # 유효한 월인가  
    if month in date:
        # 유효한 일인가      
        if int(day) <= date[month]:
            is_true = 1

    if is_true:
        print('#{} {}/{}/{}'.format(tc,data[:4],month,day))
    else:
        print('#{} {}'.format(tc, -1))
