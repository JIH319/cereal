# 16235. 나무 재테크
# 왤캐 어렵지...
# 우영님은 쉽게풀꺼야 우영님이니까
# 우영님 짱짱..
from collections import deque


def four():
    # 봄에는 나무들이 나이만큼 양분을 먹고 나이가 1 증가한다. 여러개 있으면
    # 나이가 어린 나무들이 양분을 먹고, 늙은애들은 먹지못하고 죽는다.
    for i in range(N):
        for j in range(N):
            # 나무의 갯수
            lt = len(tree[i][j])
            for k in range(lt):
                # 봄에 나무의 나이만큼 양분을 챙겨준다.
                if tree[i][j][k] <= Yang[i][j]:
                    Yang[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    # 여름에 양분을 주지못한 나무들만큼 //2를 하여 양분으로 넣어준다
                    for _ in range(k, lt):
                        Yang[i][j] += tree[i][j].pop() // 2
                    break
    # 가을 진입 가을에는 나무가 8방향으로 자라나게된다.
    for i in range(N):
        for j in range(N):
            lt = len(tree[i][j])
            for k in range(lt):
                # 나무의 나이가 5살일때,
                if tree[i][j][k] % 5 == 0:
                    for dy, dx in [(-1, -1), (0, -1), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (-1, 0)]:
                        ny = dy + i
                        nx = dx + j
                        if 0 <= nx < N and 0 <= ny < N:
                            # 왼쪽에 제일 젊은 나무들을 더해준다.
                            tree[ny][nx].appendleft(1)
            # 겨울 : 나부에 양분을 넣어준다.
            Yang[i][j] += A[i][j]


# 입력부터 보자
# 첫째 쭐에 N, M, K 가 주어진다.
N, M, K = map(int, input().split())
# 둘째 줄에 N개의 줄에 A배열의 값이 주어진다. r 번째 줄에 c번째 값은 A[r][c] 이다.
A = [list(map(int, input().split()))[:N] for _ in range(N)]
# 다음 M 개의 줄에는 상도가 심은 나무의 정보를 나타내는 세 정수 x,y,z 가 주어진다.
# 양분이 저장될 이차원 배열 생성
Yang = [[5] * N for _ in range(N)]
# 나무의 위치를 받을 이차원 배열 생성
tree = [[deque() for i in range(N)] for i in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)
for i in range(K):
    # 사계절 함수
    four()
result = 0
for i in range(N):
    for j in range(N):
        # 나무의 갯수를 result 에 넣어준다.
        result += len(tree[i][j])
print(result)
