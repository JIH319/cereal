### 1213_bkj_팰린드롬만들기

```python
import sys

def palindrome(arr,N):
    arr.sort()     # 문자열 정렬

    # 글자수가 홀수라면 >> 하나만 홀수개수
    if N & 1:
        count = 1
    # 글자수가 짝수라면 >> 모든 문자는 짝수개수
    else:
        count = 0
    i = 0               # 문자열 리스트 인덱스
    cnt = 0             # 홀수 개수의 문자가 나오면 카운팅
    palin = ['A'] * N   # palindrome 만들 리스트
    pidx = 0            # palindrome 인덱스
    # 허용 가능 홀수 개수 넘거나 인덱스가 넘으면 반복 탈출
    while cnt <= count and i+1 < N:
        if arr[i] == arr[i+1]: # 연달아 같은 수면
            palin[pidx],palin[N-1-pidx] = arr[i],arr[i+1]
            pidx += 1
            i += 2
        else:		# 홀수 글자수 일때 한개짜리 문자 >> 중간위치
            palin[N//2] = arr[i]
            i += 1
            cnt += 1
    # 팰린드롬 불가능
    if cnt > count:
        print("I'm Sorry Hansoo")
        return
    # 글자수 홀수, 마지막 글자가 회문 중간글자일때
    elif cnt < count:
        palin[pidx] = arr[-1]
    print(''.join(palin))

# data: 임한수의 영어이름 / len(data) <= 50 >> 팰린드롬 만들기
data = list(sys.stdin.readline().rstrip())
N = len(data)
palindrome(data, N)
```





### 10761_신뢰

```python
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
    # B_num, O_num = len(b_robot),len(o_robot)
    
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
    
```



### 17070_bkj_파이프 옮기기

```python
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

        
# 문제에선 (r,c)는 (1,1)부터 시작, (N,N)까지 도착할 수 있다면 >> 방법의 수 / 없다면 >> 0
# 파이프끝부분 (0,1)부터 시작, (N-1,N-1) 도착점으로 풀이
N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt = 0
dfs2(0,1,0)

print(cnt)
```

