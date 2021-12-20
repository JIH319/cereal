## [1차] 다트게임

```python
comp1 = {'S':1,'D':2,'T':3}
comp2 = {'*','#'}

def solution(dartResult):
    stack = []
    temp =''
    for e in dartResult:
        # S,D,T 나올때까지 숫자는 누적 (1,0,10 구분을 위해)
        if e in comp1:
            stack.append(int(temp)**comp1[e])
            temp = ''
        # * or # 나오면 계산
        elif e in comp2:
            if e == '*':
                # 그 뒤에 다시 *이 나올 경우 대비
                stack[-1] = stack[-1]*2
                if len(stack) >=2:
                    stack[-2] = stack[-2]*2
            else:
                stack[-1] = -stack[-1]

        else:
            temp += e
    return sum(stack)
```





---

## [1차] 비밀지도

```python
def solution(n, arr1, arr2):
    map1 = []
    map2 = []
    for e in arr1:
        map1.append(calc(n,e))
    for e in arr2:
        map2.append(calc(n,e))
    
    answer = []
    for i in range(n):
        temp = ''
        for j in range(n):
            if not map1[i][j] and not map2[i][j]:
                temp+= ' '
            else:
                temp+='#'
        answer.append(temp)
    
    return answer

def calc(n,num):
    temp = [0]*n
    for i in range(n):
        temp[n-1-i] = num%2
        num//=2
    return temp
```



## 크레인 인형뽑기 게임

```python
def solution(board, moves):
    answer = 0
    stack = []
    N = len(board)
    for e in moves:
        for i in range(N):
            # 해당 열의 위에서부터 값이 나올때까지 내려간다
            if board[i][e-1]:
                # 스택 안에 이미 인형있으면 같은지 비교
                if stack and stack[-1] == board[i][e-1]:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(board[i][e-1])
                # 해당 칸의 인형은 뽑음 처리
                board[i][e-1] = 0
                break

    return answer
```



## 키패드 누르기

```python
l = {1,4,7}
r = {3,6,9}
map = {
    1:(0,0),
    2:(0,1),
    3:(0,2),
    4:(1,0),
    5:(1,1),
    6:(1,2),
    7:(2,0),
    8:(2,1),
    9:(2,2),
    0:(3,1)
}
def solution(numbers, hand):
    answer = ''
    # 시작점의 좌표로 초기화
    right = (3,2)
    left = (3,0)
    for e in numbers:
        # 무조건 오른손으로 누를 번호
        if e in r:
            answer += 'R'
        # 무조건 왼손으로 누를 번호
        elif e in l:
            answer += 'L'
        # 거리 비교 필요 >> 좌표 차이 절대값
        else:
            tmp = map[e]
            tmp1 = abs(tmp[0]-right[0]) + abs(tmp[1]-right[1])
            tmp2 = abs(tmp[0]-left[0]) + abs(tmp[1]-left[1])
            if tmp1>tmp2:
                answer += 'L'
            elif tmp1<tmp2:
                answer += 'R'
            # 거리가 같다 >> 무슨손잡이냐에 따라 결정
            else:
                if hand == 'right':
                    answer += 'R'
                else:
                    answer += 'L'
        # 마지막 번호 누른 손은 손가락 위치 옮기기
        if answer[-1] == 'R':
            right = map[e]
        else:
            left = map[e]
    return answer
```





## 숫자 문자열과 영단어

```python
num ={
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}
def solution(s):
    answer = ''
    tmp = ''
    for e in s:
        if '0'<=e<='9':
            answer += e
        else:
            tmp += e
            if tmp in num.keys():
                answer += num[tmp]
                tmp = ''
    return int(answer)
```





## 실패율

```python
def solution(N, stages):
    answer = [(x,0) for x in range(1,N+1)]
    # cnt : i(1~N)이 나온 횟수
    # tmp : 스테이지에 도달한 플레이어 수
    cnt = 0   
    tmp = len(stages)
    for i in range(1,N+1):
        cnt = stages.count(i)
        answer[i-1] = (i,(cnt/tmp))
        tmp -= cnt
        # 다음 스테이지 부터는 도달한 플레이어 0 >> 실패율 0%
        if not tmp:
            break
        
    answer.sort(key = lambda x:(-x[1],x[0]))
    result =[]
    for i in range(N):
        result.append(answer[i][0])       
    return result
```





## 신규 아이디 추천

```python
data = {'-','_','.'}
def solution(new_id):
    
    # 1번. 소문자 치환
    new_id = list(new_id.lower())

    # idx: 뒤에서부터 문자를 가르킬 인덱스
    idx = idx = len(new_id)-1  
    # 2번.  정해진 문자 이외의 문자 제거
    while idx >= 0 :  
        if 'a' <= new_id[idx] <= 'z' or new_id[idx] in data or '0'<= new_id[idx] <='9':                 pass                          
        # 소문자와 정해진 문자가 아닐 경우 >> pop
        else:
            new_id.pop(idx)
        idx -= 1
    
    # 3번. 연속된 . 제거
    idx = len(new_id)-1
    while idx >= 0:
        if idx-1 >= 0 and new_id[idx] == '.' and new_id[idx-1] == '.':
            new_id.pop(idx)
        idx -= 1

    # 4번. 맨앞 맨뒤의 마침표 제거
    if new_id and new_id[0] == '.':
        new_id.pop(0)
    if new_id and new_id[-1] == '.':
        new_id.pop()
    
    # 5번. 빈문자열이 되었으면 'a'대입
    if not new_id:
        return 'aaa'
    
    # 6번 15개의 문자만 >> 맨 뒤 문자가 마침표라면 제거
    elif len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id.pop()
    # 7번 길이가 2 이하라면, 마지막 문자를 길이가 3 될때까지 덧붙여준다
    else:
        while len(new_id) < 3:
            new_id.append(new_id[-1])
            
    return ''.join(new_id)
```

