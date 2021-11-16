'''
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
#4
'''
# 각 회의 I에 대해 시작시간과 끝나는 시간
# 한 회의가 끝나는 것과 동시에 다음 회의가 시작 가능

def timeTable():
    start = 0
    cnt = 0
    for i in range(N):
        # 시작시간이 이전 회의보다 같거나 늦게
        if time[i][0] >= start:
            # 회의마치는시간을 start에 넣어줌 >> 다음 회의 시작시간과 비교
            start = time[i][1]
            cnt += 1
    print(cnt)

import sys

N = int(sys.stdin.readline())
time = []
for _ in range(N):
    s,e = map(int,sys.stdin.readline().split())
    time.append((s,e))
# 끝나는 시간이 이른 순으로 정렬
# ??? 틀리길래 마치는시각 같은것들 사이에서도 정렬이 필요한가해서
# x[0] 추가했더니 맞았다...테케 뭘까...?....
time.sort(key=lambda x:(x[1],x[0])) 
timeTable()