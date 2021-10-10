import sys
from collections import deque

def spring_summer(arr):
    for i in range(N):
        for j in range(N):
            # 나무가 심어져 있다면
            if arr[i][j]:
                dead = 0
                
                # 0번인덱스(k)부터 탐색
                for k in range(len(arr[i][j])):
                    
                    # 같은위치의 양분이 나무의 나이 이상이면
                    if farm[i][j] >= arr[i][j][k]:
                        # 나무의 나이만큼 양분 차감, 나이 +1
                        farm[i][j] -= arr[i][j][k]
                        arr[i][j][k] += 1

                    # 1.봄에 죽고 여름에 죽은나무가 양분이 되는 것이기 때문에
                    # 죽은 나무한테 얻은 양분을 따로 dead 변수에 저장하지 않으면 출력 오류 
                    # 2.죽은 나무를 0으로 처리하고 정렬후에 0인값만 삭제하는 반복문 생성시 시간초과
                    
                    # 나무의 나이보다 양분이 적으면 해당 나무 포함 나머지 나무들 전부 죽음
                    # appendleft로 삽입할때 정렬되기 때문
                    else:
                        # 양분이 부족해진 시점 k 부터 남은 나무의 수 만큼 실행
                        for _ in range(k,len(arr[i][j])):
                            dead += arr[i][j].pop() // 2
                        farm[i][j] += dead
                        break
              
               


def Fall_winter(arr):

    for i in range(N):
        for j in range(N):
            # i,j 돌면서 양분 로봇 활동(겨울)
            farm[i][j] += S2D2[i][j]
            for k in range(len(arr[i][j])):
                if arr[i][j][k] % 5 == 0:
                    for d in range(8):
                        nx = i + dx[d]
                        ny = j + dy[d]
                        if 0<=nx<N and 0<=ny<N:
                            farm_tree[nx][ny].appendleft(1)


    
dx = [-1,-1,0,1,1,1,0,-1] # 상 우상 우 우하 하 하좌 좌 좌상
dy = [0, 1, 1,1,0,-1,-1,-1]

N,M,K = map(int,sys.stdin.readline().split()) # K년이 지난 후 살아남은 나무의 수를 출력하자


# N개의 줄에 걸쳐 A배열의 값이 주어진다.(최초 양분과 S2D2로봇이 겨울에 뿌리는 양분)
S2D2 = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# r과 c는 1부터 시작한다.
# N*N 의 크기의 땅을 구매했다.
farm = [[5]*N for _ in range(N)]

# 나무를 심어줄 3차원 밭 배열을 하나 더 만들어준다.
farm_tree = [[deque() for _ in range(N)] for _ in range(N)]


# M개의 줄에는 상도가 심은 나무의 정보를 나타내는 정수 x,y,z 가 주어진다. x,y는 나무의 위치 z는 나무의 나이
# 나무를 심어준다.
for _ in range(M):
    x,y,z = map(int,sys.stdin.readline().split())
    farm_tree[x-1][y-1].append(z)

cnt = 0
key = 0

while K > 0:
    spring_summer(farm_tree)
    # 밭에 나무가 하나도 없다면 바로 break
    if not farm_tree:
        key = 1
        break

    Fall_winter(farm_tree)
    K -= 1


# key 가 체크되지 않았다면 나무의 개수를 세고 체크되었다면 바로 0출력
if not key:
    for i in range(N):
        for j in range(N):
            cnt += len(farm_tree[i][j])

print(cnt)