# 1. boj1213_팰린드롬만들기

```python
name = input()
N = len(name)
# 이름 속 알파벳의 갯수를 dictionary로 표현
alphabet = {}
# 각 알파벳의 값을 0으로 해주고 이후에 +=1 해줘서 갯수 알려주기
for i in name:
    alphabet[i] = 0
for i in name:
    alphabet[i] += 1

A = list(alphabet.values())
K = list(alphabet.keys())
K = sorted(K)

odd = 0
odd_alphabet = ''

for i in A:
    if i % 2:
        odd += 1
left = ''
right = ''

tmp = 0
success = 1

if odd >= 2:
    success = 0

else:
    for k in K:
        if alphabet.get(k) % 2 == 1:
            if odd_alphabet:
                success = 0
                break
            else:
                odd_alphabet = k
        tmp = alphabet.get(k)
        half_tmp = tmp//2
        for i in range(half_tmp):
            left += k
            right = k + right

# 전체 회문 만들기
if success:
    left += odd_alphabet
    result = left + right
    print(result)
else:
    print("I'm Sorry Hansoo")

```



# 2. swea10761_신뢰

```python
for tc in range(1, int(input()) + 1):
    data = input().split()
    N = int(data[0])  # 눌러야하는 버튼의 수 1 <= N <= 100

    # b_robot : B로봇이 들러야할 위치, 버튼 누를 위치 담을 리스트
    # o_robot : O로봇이 들러야할 위치, 버튼 누를 위치 담을 리스트
    b_robot, o_robot = [], []  # B로봇, O로봇 시작위치 1
    order = []  # order : 순서 담은 리스트
    for i in range(N):
        if data[2 * i + 1] == 'B':
            order.append('B')
            b_robot.append(int(data[2 * i + 2]))
        else:
            order.append('O')
            o_robot.append(int(data[2 * i + 2]))

    # b_robot: [2, 4]
    # o_robot: [1, 2]
    # order: ['B', 'O', 'O', 'B']

    ########################################################

    bidx, oidx = 0, 0 # 현재 해당 로봇의 인덱스
    b, o = 1, 1  # 현재 위치
    # B로봇, O로봇이 들러야하는 공간의 개수
    # B_num, O_num = len(b_robot),len(o_robot)

    # B,O 로봇 둘 다 마지막 요소에 도착할 때까지 반복
    idx = 0  # order 가리키는 변수
    time = 0
    while idx < N: #마지막 차례가 될 때까지
        current = order[idx]  # current : 현재 버튼 누를 로봇이 B/O인지

        # 버튼 누를 로봇이 Blue라면
        if current == 'B':
            tmp = abs(b_robot[bidx] - b) + 1   # 이전 위치에서 현재 위치 이동 시간 + 버튼 누르는 시간
            b = b_robot[bidx]                  # b로봇 위치 이동
            bidx += 1                         #현재 로봇의 idx이기 때문에 +1
            idx += 1                          # order가 가리키는 변수 +1 다음 버튼 check

            if idx < N and 'O' in order[idx:]:   
                # 아직 누를 버튼이 남아있고, 남은 순서에 오렌지 로봇이 있다면? 오렌지 로봇이동
                # Blue가 이동하는 동안 orange도 다음 위치까지 가기 힘든 경우 >> 시간만큼 더해줌
                if abs(o_robot[oidx] - o) > tmp: 
                    # 오렌지 로봇이 눌러야하는 버튼으로 이동하는 값이 tmp보다 크면
                    if o_robot[oidx] > o:  # 오렌지가 누를 버튼 위치가 현재 위치한 곳보다 클 경우,
                        o += tmp # 현재위치를 tmp만큼 옮겨주고
                    else:
                        o -= tmp 
                        # 오렌지가 누를 버튼 위치가 현재 위치한 곳보다 작을 경우, 
                        # 현재위치를 tmp만큼 빼준다. (과거로 돌아감)

                # 이동시간이 충분히 커서 다음 위치까지 이동 가능하다면
                elif abs(o_robot[oidx] - o) <= tmp:
                    o = o_robot[oidx] # 오렌지의 위치는 오렌지가 가야하는 버튼의 위치까지

            time += tmp  # 총 걸린 시간 += 위치 이동시간, 버튼 누르는 시간

        # 버튼 누를 로봇이 Orange라면
        else:
            tmp = abs(o_robot[oidx] - o) + 1  # 이전 위치에서 현재 위치 이동 시간 + 버튼 누르는 시간
            o = o_robot[oidx]
            oidx += 1
            idx += 1

            if idx < N and 'B' in order[idx:]:  # 남은 순서에 O로봇이 있다면,
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
    print('#{} {}'.format(tc, time))
```

