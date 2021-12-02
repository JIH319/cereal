# 신규 아이디 추천

```python
def solution(new_id):

    new_id = new_id.lower()

    answer = ''
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word

    while '..' in answer:
        answer = answer.replace('..', '.')

    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer

    answer = 'a' if answer == '' else answer

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
            
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3-len(answer))
    return answer
```



# 숫자 문자열과 단어

```python
num_dict = {'zero': '0', 'one': '1', 'two': '2', 'three':'3', 'four': '4', 'five': '5', 'six': '6', 'seven':'7', 'eight':'8', 'nine':'9'}
def solution(s):
    for k, v in num_dict.items():
        s = s.replace(k, v)
    return int(s)
```



# 키패드 누르기

```python
def solution(numbers, hand):
    lt = 10
    rt = 12
    answer = ''
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            lt = n
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            rt = n   
        else:
            temp = 11 if n == 0 else n
            temp1, temp2 = abs(temp-lt), abs(temp-rt)
            temp1 = temp1//3 + temp1%3
            temp2 = temp2//3 + temp2%3
            if temp1 == temp2:
                if hand == 'right':
                    rt = temp
                    answer += 'R'
                else:
                    lt = temp
                    answer += 'L'
            elif temp1 > temp2 :
                rt = temp
                answer += 'R'
            else:
                lt = temp
                answer += 'L'
    return answer
```



# 크레인 인형뽑기 게임

```python
def solution(board, moves):
    a = []
    count = 0
    for i in moves:
        for j in range(len(board)) :
            if board[j][i-1] is not 0 :
                if len(a) != 0 and a[-1] == board[j][i-1] :
                    del a[-1]
                    count +=2
                else :
                    a.append(board[j][i-1])
                board[j][i-1] = 0
                break
    return count
```



# 실패율

```python
def solution(N, stages):
    answer = []
    leng = len(stages)
    for i in range(1, N+1):
        count = stages.count(i)
        if leng == 0 :
            fail = 0
        else :
            fail = count / leng
        
        answer.append((i, fail))
        leng -= count
    
    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer
```



# 비밀지도

```python
# 비트연산자를 사용했고, bin 함수를 이용해 이진수로 바꿔준 뒤, zfill로 앞 부분에 0을 채워줌
# replace로 1은 '#', 0은 공백으로 바꿔주었다. 파이썬 내장함수로 손쉽게 풀리는 문제였다.

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(bin(arr1[i] | arr2[i])[2:].zfill(n).replace('1','#').replace('0',' '))
    return answer
```



# 다트 게임

```python
def solution(dartResult):
    # S, D, T
    # * 스타상(해당점수, 전의 점수 2배) # 아차상 (해당 점수 마이너스)
    i = 0
    stack = []
    while i < len(dartResult):
        if dartResult[i].isdecimal():
            if dartResult[i+1].isdecimal():
                stack.append(10)
                i+=2
                continue
            else:
                stack.append(int(dartResult[i]))
                i += 1
        else:
            if dartResult[i] == 'S':
                pass
            elif dartResult[i] == 'D':
                stack[-1] **=2
            elif dartResult[i] == 'T':
                stack[-1] **=3
            elif dartResult[i] == '*':
                stack[-1] *= 2
                if len(stack) > 1:
                    stack[-2] *= 2
            elif dartResult[i] == '#':
                stack[-1] *= -1
            i += 1
    return sum(stack)
```

