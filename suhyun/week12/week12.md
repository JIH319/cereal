#### Lv1. 신규 아이디 추천

```python
def solution(new_id):
    # 1 단계. 대문자를 소문자로 치환
    rst1 = new_id.lower()
    # 2 단계. 사용가능한 문자를 제외하고 제거
    rst2 = ''
    cnt3 = False
    for n in rst1:
        if '0'<=n<='9' or 'a'<=n<='z' or n == '-' or n =='_':
            rst2 += n
            cnt3 = False
        # 3 단계. 마침표가 2번이상 연속된 부분은 하나의 마침표로 치환.
        if n =='.' and not cnt3:
            rst2 += n
            cnt3 = True
    # 4 단계. 양쪽 끝 마침표 제거 (strip 사용)
    rst2 = rst2.strip('.')
    # 5 단계. new_id 가 빈 문자열 일 경우, a 를 대입
    if not rst2:
        rst2 += 'a'
    # 6 단계. new_id 가 16자 이상이라면, 첫 15개 문자를 제외하고 나머지 문자 모두 제거, 마침표일경우 마침표도 제거
    if len(rst2)>=16:
        rst2 = rst2[:15]
    answer = rst2.rstrip('.')
    # 7 단계. new_id 가 2자 이하라면, new_id 의 마지막 문자를 new_id 의 길이가 3이 될때 까지 반복.
    while len(answer)<=2:
        answer += answer[-1]
    return answer

# 아이디 길이는 3자이상 15자 이하
# 아이디는 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표 만 사용가능
# . 는 처음과 끝에 사용할 수 없고 연속으로도 사용 불가

```



#### Lv1. 숫자 문자열과 영단어

```python
num_dict = {
    'zero':'0','one':'1','two':'2',
    'three':'3','four':'4','five':'5',
    'six':'6','seven':'7','eight':'8',
    'nine':'9'
}

def solution(s):
    # 문자열이 주어진다면, 그 문자열이 그냥 숫자인경우는 바로넣어주고,
    # 문자가 주어진다면 해당하는 글자를 숫자로 바꿔서 저장해주자.
    answer = ''
    i = 0
    while i < len(s):
        # 숫자일 경우, 바로넣어주고 i를 올리자.
        if '0'<=s[i]<='9':
            answer += s[i]
            i += 1
        else:
            # 문자일 경우, 빈 문자열을 받아주고,
            tmp = ''
            # 숫자가 나오기 전까지나, s 의 길이를 벗어나지 않는다면, while 반복문을 도는데,
            while not '0'<=s[i]<='9' and i< len(s):
                tmp += s[i]
                i += 1
                # num_dict 에서 설정한 키 값에 포함될 경우, break 해주고 answer 에 담아주자.
                if tmp in num_dict.keys():
                    break
            answer += num_dict[tmp]
    # 출력으로 필요한 것은 숫자형, int로 변환해주자.
    answer = int(answer)
    
    return answer

```



#### Lv1. 키패드 누르기

```python
# 절대 값을 구해주는 사용자 정의 함수
def absolute(n):
    if n>0:
        return n
    else:
        return -n

def solution(numbers, hand):
    answer = ''
    # 우선 생각해보자. [1,4,7] 은 왼손, [3,6,9] 는 오른손, [2,5,8,0]은 거리에 따라, 같을 경우 hand 를 따른다.
    # 그렇다면 눌렀을떄의 위치도 저장하여, [2,5,8,0] 일 때의 거리도 알아야 겠네!
    # [2,5,8,0] 에 이미 위치해있을 경우도, 거리로 계산해야하네! , 그러다 [1,4,7], [3,6,9] 위치로 갈떄는 다시 이동!
    # 왼손 현재 위치 *
    lc = [3,0]
    # 오른손 현재 위치 #
    rc = [3,2]
    for number in numbers:
        # 왼손 하나로 뭉쳐주기!
        if number%3==1 and number!=0:
            lc = [number//3,0]
            answer +='L'
        # 오른손 하나로 뭉쳐주기!
        elif number%3==0 and number!=0:
            rc = [number//3-1,2]
            answer += 'R'
        # 중간인 경우도 뭉쳐주자
        elif number%3 == 2:
            if absolute(lc[0]-number//3)+absolute(lc[1]-1)>absolute(rc[0]-number//3)+absolute(rc[1]-1):
                rc = [number//3,1]
                answer += 'R'
            elif absolute(lc[0]-number//3)+absolute(lc[1]-1)==absolute(rc[0]-number//3)+absolute(rc[1]-1):
                if hand == 'left':
                    lc = [number//3,1]
                    answer += 'L'
                else:
                    rc = [number//3,1]
                    answer += 'R'
            else:
                lc = [number//3,1]
                answer +='L'
        # 0 인 경우는 특이하니까 빼주자.
        elif number == 0:
            if absolute(lc[0]-3)+absolute(lc[1]-1)>absolute(rc[0]-3)+absolute(rc[1]-1):
                rc = [3,1]
                answer += 'R'
            elif absolute(lc[0]-3)+absolute(lc[1]-1)==absolute(rc[0]-3)+absolute(rc[1]-1):
                if hand == 'left':
                    lc = [3,1]
                    answer += 'L'
                else:
                    rc = [3,1]
                    answer += 'R'
            else:
                lc = [3,1]
                answer +='L'
                                                          
    return answer
```



#### Lv1. 크레인 인형뽑기 게임

```python
def solution(board, moves):
    # 정사각 격자이므로, n 의 길이는 항상 구할 수 있다.
    n = len(board)
    # moves 로 이동시키고, 그게 애니팡~ 이 되버리면 날라가며, 그 갯수를 샌다. 2개가 사라지므로 결과값은 항상 짝수
    # 저장할 배열을 구해주자.
    stack = [0]
    answer = 0
    for move in moves:
        for i in range(n):
            if board[i][move-1]:
                # move 는 1 부터 시작하는 데, 배열은 0부터 시작하니까 -1해주고 시작
                # 기존에 담긴 stack 과 일치하면 +=2 해주면서 pop 만해주고 사용한건 0으로,
                if stack[-1]==board[i][move-1]:
                    stack.pop()
                    answer += 2
                    board[i][move-1] = 0
                    break
                # 그게 아니라면, stack에 넣어주고, 사용한건 0으로
                else:
                    stack.append(board[i][move-1])
                    board[i][move-1] = 0
                    break
    return answer
```



#### Lv1. 실패율

```python
# 오렐리는 슈퍼개발자래.. .멋지다.. 완전 쩔어
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수/ 스테이지에 도달한 플레이어 수

def solution(N, stages):
    rst = {}
    # 총 도전하는 유저의 수
    users = len(stages)
    # 1 스테이지 부터 시작하므로, 범위는 1~ N 까지
    for s in range(1,N+1):
        # 유저가 있는 동안에는, 딕셔너리로 key 는 stage, value는 실패율로 넣어주자.
        if users != 0:
            rst[s] = stages.count(s)/users
            users -= stages.count(s)
        else:
             rst[s] = 0
    # 함수 출력, rst 의 key를 rst value 의 내림차순으로 정렬해준다.
    answer = sorted(rst.keys(),key=lambda x: rst[x],reverse=True)
    return answer

```



#### Lv1. 비밀지도

```python
# 2진법으로 해당 값을 변경해주는 함수.
def binary(x,y):
    rst = []
    while x-1>-1:
        if y//(2**(x-1)):
            y-=2**(x-1)
            x -=1
            rst.append(1)
        else:
            x -=1
            rst.append(0)
    return rst

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        result = ''
        # 두개의 배열에서 한줄을 가져온뒤에,
        rst1 = binary(n,arr1[i])
        rst2 = binary(n,arr2[i])
        # 하나씩 돌아가면서, 둘다 0 인경우는 공백을, 둘 중 하나라도 1 인경우는 # 을 출력하도록한다.
        for j in range(n):
            if not rst1[j] and not rst2[j]:
                result += ' '
            else:
                result += '#'
        # 그리고 해당 값을 answer 에 append 해준다.
        answer.append(result)
    return answer
```



#### Lv1. 다트 게임

```python

def solution(dartResult):
    answer = 0
    # 싱글이면 1, 더블이면 2, 트리플이면 3을 딕셔너리를 활용하여 부른다.
    dart_dict = {'S':1,'D':2,'T':3}
    # 해당 값을 stack 에 저장한뒤에 나중에 합해준다.
    stack = []
    i = 0
    while i<len(dartResult):
        # 해당 값이 S D T 인경우,
        if dartResult[i] == 'S' or dartResult[i] == 'D' or dartResult[i] == 'T':
            # 10인 경우에는 10 을 가져와 제곱해주고,
            if dartResult[i-1] =='0' and dartResult[i-2] =='1':
                stack.append(int(dartResult[i-2:i])**dart_dict[dartResult[i]])
            # 그 외의 숫자인 경우는 0~9까지 자기가 알아서 들고와서 제곱해준다.
            else:
                stack.append(int(dartResult[i-1])**dart_dict[dartResult[i]])
        # * (스타상) 이 나왔을 경우,
        elif dartResult[i] =='*':
            # 아직 길이가 1이면 마지막 배열 원소만 *2 를,
            if len(stack)==1:
                stack[-1]*=2
            # 길이가 2이상이면, 마지막과 그 전 원소에 * 2 를 해준다.
            else:
                stack[-1]*=2
                stack[-2]*=2
        # # (아차상) 인 경우, 부호를 반대로 만들어준다.
        elif dartResult[i]=='#':
            stack[-1]*=-1           
        # 모든 경우에 일단 i+1은 해준다. (for 문으로해도되겠넹)
        i+=1
    # 해당 원소 stack의 값을 모두 더해주면 우리가 구하고자 하는 answer 가 된다.
    answer = sum(stack)
    return answer
```

