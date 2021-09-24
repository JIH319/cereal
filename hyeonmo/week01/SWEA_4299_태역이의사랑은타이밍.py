T = int(input())
for tc in range(1,T+1):
    D,H,M = list(map(int,input().split()))

    meet_time = (11*24+11)*60+11    # 만나기로 한 11일 11시 11분이 총 몇분인지 계산
    taehyuk_time = (D*24+H)*60+M    # 깨달음을 얻은 날짜가 총 몇분인지 계산

    if taehyuk_time > meet_time:    # 깨달음을 얻은 시간이 더 나중이라면 만나기로한 시간 차감
        taehyuk_time -= meet_time
        print(f'#{tc} {taehyuk_time}')
    elif taehyuk_time == meet_time: # 같으면 0 낮으면 -1
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {-1}')
