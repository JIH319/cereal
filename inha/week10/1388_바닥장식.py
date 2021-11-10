import sys
input = sys.stdin.readline

# 바닥 장식 몇개 필요한지 체크하는 함수
def check(arr, match):
    cnt = 0
    # 직사각형 arr의 행만큼 돔
    for i in range(len(arr)):
        # 다음 행으로 넘어갈때마다 isMatch를 False로 초기화
        isMatch = False
        # 직사각형 arr의 열만큼 돔
        for j in range(len(arr[0])):
            # isMatch가 False이면서 arr[i][j]가 찾는 문자와 똑같은 경우 cnt + 1
            # (즉, match 문자가 연속으로 올 때는 cnt +1을 해주지 않음)
            if not isMatch and arr[i][j] == match:
                isMatch = True
                cnt += 1
            # match 문자와 다른 문자가 올 경우 isMatch는 False
            elif arr[i][j] != match:
                isMatch = False
    return cnt


N, M = map(int, input().split())
floor1 = [list(input().rstrip()) for _ in range(N)]
# '|'문자는 같은 열에 있는 것을 찾아야 하므로 check함수에 적용시키기 위해 전치행렬 만듦
floor2 = [[] for _ in range(M)]
for j in range(M):
    for i in range(N):
        floor2[j].append(floor1[i][j])

print(check(floor1, '-')+check(floor2, '|'))