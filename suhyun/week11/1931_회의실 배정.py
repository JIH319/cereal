# 1931. 회의실 배정
import sys

input = sys.stdin.readline

N = int(input())  # 회의의 수
arr = [[0] * 2 for _ in range(N)]  # 회의 시간
for i in range(N):
    arr[i][0], arr[i][1] = map(int, input().split())  # 각 요소를 일단 대입해주자.

arr.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간 , 시작 시간 오름차순으로 정렬

cnt = 1  # 첫 회의는 무조건 하니까 1부터 시작
end = arr[0][1]  # 첫 회의가 끝나는 시간.
for i in range(1, N):  # 총 회의 갯수 만큼 반복문
    # 다음 회의 시작시간이 끝시간 보다 크거나 같을경우,
    if arr[i][0] >= end:
        # 그 회의의 끝시간을 대입해주고, cnt+=1 을 해준다.
        end = arr[i][1]
        cnt += 1
print(cnt)
