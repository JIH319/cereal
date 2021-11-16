'''
1. 2칸 위로, 1칸 오른쪽
2. 1칸 위로, 2칸 오른쪽
3. 1칸 아래로, 2칸 오른쪽
4. 2칸 아래로, 1칸 오른쪽

>> 재귀, DP(x: 방향기억), DFS

이동 횟수가 4번보다 적지 않다면, 이동 방법을 모두 한 번씩 사용 
이동 횟수가 4번보다 적은 경우(방문한 칸이 5개 미만)에는 이동 방법에 대한 제약이 없다.
방문할 수 있는 칸의 최대 개수
'''
dir=[(-2,1),(-1,2),(1,2),(2,1)]
move = {0:0,1:0,2:0,3:0}

def travel(r,c):
    global maxV

    visited = [[0]*M for _ in range(N)]
    visited[r][c] = 1
    stack = [(r,c)]
    while stack:
        cr,cc = stack[-1]
        # 더이상 갈 수 없으면 (종료조건 : 맨위줄 맨오른쪽줄)
        if cr == 0 or cc == M-1:
            if sum(move.values()) >= 4 and 0 in move.keys():
                return
            else:
                maxV = max(maxV,sum(move.values()))
        for i in range(4):
            nr,nc = cr+dir[i][0], cc+dir[i][1]
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc]:
                visited[nr][nc] = 1
                stack.append((nr,nc,i))
                move[i] += 1
                break
        else:
            r,c,i = stack.pop()
            move[i] -= 1

# N:세로, M:가로
N,M = map(int,input().split())

count = [[0]*M for _ in range(N)]
# 가장 왼쪽아래 칸에서 출발
# visited : 방문체크
# visited = [[0]*M for _ in range(N)]
# visited[N-1][0] = 1
maxV = 0
move = {0:0,1:0,2:0,3:0}
travel(N-1,0)

print(maxV)

# def travel(r,c,move,cnt):
#     global maxV

#     # 맨위 , 맨오른쪽칸은 더이상 진행 X
#     # 더이상 이동 X
#     # 4번이상 이동 >> 방향 검사
#     if r == 0 or c == M-1:
#         if cnt > 4:
#             if 0 not in move.values():
#                 maxV = max(maxV,cnt)
#         else:
#             maxV = max(maxV,cnt)
#         return 
    
#     # 이전보다 적은 횟수로 도착했다면, 더이상 진행 X
#     # if count[r][c] > cnt:
#     #     if cnt > 4:
#     #         if 0 not in move.values():
#     #             maxV = max(maxV,cnt)
#     #     else:
#     #         maxV = max(maxV,cnt)
#     #     return
#     # else:
#     #     count[r][c] = cnt


#     for i in range(4):
#         nr,nc = r+dir[i][0],c+dir[i][1]
#         if 0<=nr<N and 0<=nc<M:
#             # visited[nr][nc] = 1
#             move[i] += 1
#             travel(nr,nc,move,cnt+1)
#             # 되돌리기
#             # visited[nr][nc] = 0
#             move[i] -= 1
    

    # print(r,c)
    # print(move)
    # print(maxV)
    

    

# # N:세로, M:가로
# N,M = map(int,input().split())

# count = [[0]*M for _ in range(N)]
# # 가장 왼쪽아래 칸에서 출발
# # visited : 방문체크
# # visited = [[0]*M for _ in range(N)]
# # visited[N-1][0] = 1
# maxV = 0
# move = {0:0,1:0,2:0,3:0}
# travel(N-1,0,move,1)

# print(maxV)
# result = 0
# for e in visited:
#     result += sum(e)
# print(result)