T = int(input())
for tc in range(1,T+1):
    data = input().split()
    N = data.pop(0)

    sequence = []  # 먼저 버튼을 눌러야 하는 순서 ['B', 'O', 'O', 'B']
    Blue_go = []   # 먼저 목표로 가야하는 버튼의 거리 [2, 4]
    Orange_go = [] # 먼저 목표로 가야하는 버튼의 거리 [1, 2]
    result = 0 #

    for i in range(0,len(data),2):
        if data[i] == 'B':
            sequence.append(data[i])
            Blue_go.append(int(data[i+1]))

        elif data[i] == 'O':
            sequence.append(data[i])
            Orange_go.append(int(data[i + 1]))

    Blue_idx = 1 # 블루와 오렌지의 각 출발점은 1
    Orange_idx = 1

    while sequence:
        key = True  # 한쪽이 버튼을 눌렀다는 표시를 위한 키값
        result += 1 # 시간출력

        if Blue_go: # 블루가 가야할 곳이 있다면

            # 현재 위치 보다 가야할 곳이 멀다면 가깝게 다가가기
            if Blue_idx < Blue_go[0]:
                Blue_idx += 1
            elif Blue_idx > Blue_go[0]:
                Blue_idx -= 1
            # 버튼을 눌러야 될 차례에 위치가 동일하고 key가 True라면 버튼누르기
            elif sequence[0] == 'B' and Blue_go[0] == Blue_idx and key:
                sequence.pop(0)     # 눌렀으면 순서에서 제외
                Blue_go.pop(0)      # 눌렀으면 가야할 목표위치 제외
                key = False         # 키값 변경(키값이 없으면 바로 밑의 오렌지에서 동시에 버튼을 누를수 있음)

        if Orange_go: # 오렌지가 가야할 곳이 있다면
            if Orange_idx < Orange_go[0]:
                Orange_idx += 1
            elif Orange_idx > Orange_go[0]:
                Orange_idx -= 1
            elif sequence[0] == 'O' and Orange_go[0] == Orange_idx and key:
                sequence.pop(0)
                Orange_go.pop(0)
                key = False

    print('#{} {}'.format(tc,result))