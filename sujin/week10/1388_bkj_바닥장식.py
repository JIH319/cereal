def calc(target,r,c, arr):
    '''
    target: 현재 무시할 막대 (target에서 다른 막대 모양 될 때 count += 1)
    r: 세로 길이
    c: 가로 길이
    arr: 현재 바닥
    '''
    global count

    for i in range(r):
        remember = arr[i][0]
        # 가로막대로 시작했으면 일단 count 1
        if remember != target:
            count += 1
        for j in range(1,c):
            # 가로막대인데, 직전은 가로막대 X 
            # >> 방금 세로막대에서 가로막대로 바뀜 >> count += 1 
            if target != arr[i][j] and remember != arr[i][j]:
                count += 1
            remember = arr[i][j]

N,M = map(int,input().split())
# 세로:N 가로:M 
room = [input() for _ in range(N)]
# 세로:M 가로:N (원래 구조를 90도 돌림)
room2 = [[0]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        room2[i][j] = room[N-j-1][i]

count = 0
calc('|',N,M,room)
calc('-',M,N,room2)

print(count)