'''


import sys

# (r,c)는 (1,1)부터 시작, (N,N)까지 도착할 수 있다면 >> 방법의 수 / 없다면 >> 0
N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 파이프를 밀 수 있는 방향은 총 3가지 >>  →, ↘, ↓ 방향 / 45도
# dir = [(0,0,1),(1,1,1),(2,1,0)]
dir_dict = {
    0 : [(0,0,1),(1,1,1)],              # 가로, 갈 수 있는 방향 :  →, ↘
    1 : [(0,0,1),(1,1,1),(2,1,0)] ,     # 대각선, 갈 수 있는 방향 : →, ↘, ↓
    2 : [(1,1,1),(2,1,0)]               # 세로, 갈 수 있는 방향 : ↘, ↓
}
cnt = 0
selected = [[0]*N for _ in range(N)]
stack = [(0,0,1)]   # [0] : 시작 파이프 방향, (0,1) : 시작 좌표
selected[0][1] = 1
while stack:
    d,cr,cc = stack[-1]
    if (cr,cc) == (N-1,N-1):
        cnt += 1
    for dir, dr,dc in dir_dict[d]:
        nr,nc = cr+dr, cc+dc
        # 범위 밖, 방문한 곳이면, 벽인 곳 >>  다음 반복
        if 0>nr or nr >= N or 0>nc or nc >= N or selected[nr][nc] or arr[nr][nc]:continue
        # 가로로 있을때,이동할 바로 옆에 벽또는 좌표 밖일때 >> 나아갈 수 없음
        # 세로로 있을때,이동할 바로 아래에 벽또는 좌표 밖일때 >> 나아갈 수 없음
        if (nr < N-1 and arr[nr+1][nc] == 1 and dir == 2) or (nc < N-1 and arr[nr][nc+1] == 1 and dir == 0):continue
        if (nr,nc) != (N-1,N-1) and (nr == N-1 and dir == 2) or (nc == N-1 and dir == 0):continue
        selected[nr][nc] = 1
        stack.append((dir,nr,nc))
        print(dir,'방향으로', nr, nc,'좌표로 이동')
        break
    else:
        dir,pr,pc = stack.pop()
        print(dir,pr,pc)
        selected[pr][pc] = 0
print(cnt)


import sys

# (cr,cc) : 현재 위치 좌표 / d : 현재 파이프 모양 (0:가로, 1:대각선, 2:세로)
def dfs(cr,cc,d):
    global cnt
    for dir, dr,dc in dir_dict[d]:
        nr,nc = cr+dr, cc+dc
        # 범위 안, 미방문한 곳이면, 벽이 아닌 곳
        if 0<=nr<N and 0<=nc<N and not arr[nr][nc]:
            
            # 대각선으로 갈 때는 그 옆 위칸이 벽(1)이 아니어야한다
            if dir == 1 and (arr[nr-1][nc] or arr[nr][nc-1]):
                continue

            # 목표 도착점이면 cnt 올리고 돌아가자
            if (nr,nc) == (N-1,N-1):
                cnt += 1
                # print('도착')
                return

            # 파이프가 가로인데 맨끝 이거나 세로인데 맨밑이면 
            if (dir == 0 and nc == N-1) or (dir == 2 and nr == N-1):
                continue
            
            # 목표 도착점 아니면 더 찾자
            # print(dir,'방향으로 (',cr,cc,')에서  (',nr,nc,')')
            dfs(nr,nc,dir)

def dfs2(r,c,d):
    
    (r,c) : 현재 파이프 좌표
    d : 파이프가 놓여진 방향 ex) 0 : 가로, 1 : 대각선, 2 : 세로
    
    global cnt
    # 도착성공
    if (r,c) == (N-1,N-1):
        cnt += 1
        return
    # 범위밖이거나 벽이면 return
    if r<0 or r>=N or c<0 or c>=N or arr[r][c]:
        return
    # 범위안, 벽도 아닐때, 방향 대각선이면 그 위 아래 체크
    else:
        if d == 1 and (arr[r-1][c] or arr[r][c-1]):
            return

    # 가로 방향일때, 가로 대각선 가능
    if d == 0:
        dfs2(r,c+1,0)
        dfs2(r+1,c+1,1)
    # 대각선 방향일때, 가로 대각선 세로 가능
    elif d == 1:
        dfs2(r,c+1,0)
        dfs2(r+1,c+1,1)
        dfs2(r+1,c,2)
    # 세로 방향일때, 대각선 세로 가능
    else:
        dfs2(r+1,c+1,1)
        dfs2(r+1,c,2)

        


# (r,c)는 (1,1)부터 시작, (N,N)까지 도착할 수 있다면 >> 방법의 수 / 없다면 >> 0
N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 파이프를 밀 수 있는 방향은 총 3가지 >>  →, ↘, ↓ 방향 / 45도
# dir = [(0,0,1),(1,1,1),(2,1,0)]
dir_dict = {
    0 : [(0,0,1),(1,1,1)],              # 가로, 갈 수 있는 방향 :  →, ↘
    1 : [(0,0,1),(1,1,1),(2,1,0)] ,     # 대각선, 갈 수 있는 방향 : →, ↘, ↓
    2 : [(1,1,1),(2,1,0)]               # 세로, 갈 수 있는 방향 : ↘, ↓
}
cnt = 0

dfs2(0,1,0)
print(cnt)

'''

import sys

def dfs2(r,c,d):
    '''
    (r,c) : 현재 파이프 좌표
    # 파이프를 밀 수 있는 방향은 총 3가지 >>  →, ↘, ↓ 방향 / 45도
    d : 파이프가 놓여진 방향 ex) 0 : 가로, 1 : 대각선, 2 : 세로
    '''
    global cnt
   
    # 도착성공
    if (r,c) == (N-1,N-1):
        cnt += 1
        return

    # 가로 방향일때, 가로 대각선 가능
    if d == 0:
        # 가로 >> 밀었을 때 벽에 맞닿으면 안됨
        if c + 1 < N and arr[r][c+1] == 0:
            dfs2(r,c+1,0)
        # 대각선 >> 밀었을 때 위칸, 아래칸이 벽(1)이면 안됨
        if r + 1 < N and c + 1 < N and arr[r+1][c+1] == 0 and arr[r+1][c] == 0 and arr[r][c+1] == 0:
            dfs2(r+1,c+1,1)
    # 대각선 방향일때, 가로 대각선 세로 가능
    elif d == 1:
        # 가로 >> 밀었을 때 벽에 맞닿으면 안됨
        if c + 1 < N and arr[r][c+1] == 0:
            dfs2(r,c+1,0)
        # 대각선 >> 밀었을 때 위칸, 아래칸이 벽(1)이면 안됨
        if r + 1 < N and c + 1 < N and arr[r+1][c+1] == 0 and arr[r+1][c] == 0 and arr[r][c+1] == 0:
            dfs2(r+1,c+1,1)
        # 세로 >> 밀었을 때 벽에 맞닿으면 안됨
        if r + 1 < N and arr[r+1][c] == 0:
            dfs2(r+1,c,2)
    # 세로 방향일때, 대각선 세로 가능
    else:
        # 대각선 >> 밀었을 때 위칸, 아래칸이 벽(1)이면 안됨
        if r + 1 < N and c + 1 < N and arr[r+1][c+1] == 0 and arr[r+1][c] == 0 and arr[r][c+1] == 0:
            dfs2(r+1,c+1,1)
        # 세로 >> 밀었을 때 벽에 맞닿으면 안됨
        if r + 1 < N and arr[r+1][c] == 0:
            dfs2(r+1,c,2)

        
# (r,c)는 (1,1)부터 시작, (N,N)까지 도착할 수 있다면 >> 방법의 수 / 없다면 >> 0
N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt = 0

dfs2(0,1,0)

print(cnt)