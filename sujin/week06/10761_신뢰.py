'''
3
4 B 2 O 1 O 2 B 4
3 B 5 B 8 O 100
2 O 2 O 1

#1 6
#2 100
#3 4
'''

for tc in range(1, int(input())+1):
    data = input().split()
    N = int(data[0])         # 눌러야하는 버튼의 수 1 <= N <= 100

    # b_robot : B로봇이 들러야할 위치, 버튼 누를 위치 담을 리스트
    # o_robot : O로봇이 들러야할 위치, 버튼 누를 위치 담을 리스트
    b_robot, o_robot = [],[]    # B로봇, O로봇 시작위치 1
    order = []                    # order : 순서 담은 리스트
    for i in range(N):
        if data[2*i+1] == 'B':
            order.append('B')
            b_robot.append(int(data[2*i+2]))
        else:
            order.append('O')
            o_robot.append(int(data[2*i+2]))

    # bidx,oidx : 현재 해당 로봇의 인덱스
    bidx,oidx = 0,0
    b , o = 1,1     # b,o 현재 위치
    # B로봇, O로봇이 들러야하는 공간의 개수 
    
    # B,O 로봇 둘 다 마지막 요소에 도착할 때까지 반복
    idx = 0     # order 가르킬 변수
    time = 0
    while idx < N:
        # 버튼 K는 시작점에서 K 미터 떨어져 있음
        # 매초 선택지 1. 1미터 건기 2. 버튼 누르기 3. 아무것도 하지 않기
        current = order[idx]    # current : 현재 버튼 누를 로봇
        if current == 'B':
            tmp = abs(b_robot[bidx] - b) + 1 # 이전 위치에서 현재 위치 이동 시간 + 버튼 누르는 시간
            b = b_robot[bidx]   # b로봇 위치 이동
            bidx += 1
            idx += 1
            if idx < N and 'O' in order[idx:]:  # 남은 순서에 O로봇이 있다면>> o로봇이동
                # 현재 B가 이동하는 동안 다음 위치까지 가긴 힘듬 >> 시간만큼 더해줌 
                if abs(o_robot[oidx] - o) > tmp:
                    if o_robot[oidx] > o:
                        o += tmp
                    else:
                        o -= tmp
                # 이동시간이 충분히 커서 다음 위치까지 이동 가능 
                elif abs(o_robot[oidx] - o) <= tmp:
                    o = o_robot[oidx] 
            
            time += tmp  # 위치 이동시간, 버튼 누르는 시간


        else:
            tmp = abs(o_robot[oidx] - o)  + 1 # 이전 위치에서 현재 위치 이동 시간 + 버튼 누르는 시간
            o = o_robot[oidx]
            oidx += 1
            idx += 1
            
            if  idx < N and 'B' in order[idx:]:  # 남은 순서에 O로봇이 있다면, 
                # 현재 B가 이동하는 동안 다음 위치까지 가긴 힘듬 >> 시간만큼 더해줌 
                if abs(b_robot[bidx] - b) > tmp:
                    if b_robot[bidx] > b:
                        b += tmp
                    else:
                        b -= tmp
                # 이동시간이 충분히 커서 다음 위치까지 이동 가능 
                elif abs(b_robot[bidx] - b) <= tmp:
                    b = b_robot[bidx]
            
            time += tmp  # 위치 이동시간, 버튼 누르는 시간
        # print('이번엔 ',tmp)
    print('#{} {}'.format(tc,time))
    
