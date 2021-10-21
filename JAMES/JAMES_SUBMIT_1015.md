

# 팰린드롬 만들기

```python
# 임한수와 임문빈은 서로 사랑하는 사이이다.?
# 임한수는 세상에서 팰린드롬인 문자열을 너무 좋아하기 때문에, 둘의 백일을 기념해서 임문빈은 팰린드롬을 선물해주려고 한다.? 사랑의 힘이란...
# 임문빈은 임한수의 영어 이름? 으로 팰린드롬을 만들려고 하는데,,아 외국인 갬성이면 ㅇㅈ
# 임문빈을 도와 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램을 작성해보자 ㅇㅋㅇㅋ

# 1. 문빈이한테서 한수 이름을 받는다
hansu_name = input()
# 2. 해당 알파벳이 몇개나 나왔나 개수를 세릴 카운트리스트를 만들고
cnt = [0 for _ in range(26)]
# 3. 다 대문자에 A가 65니께 ex) A이면 0부터 1씩 넣어준다
for alphabet in hansu_name:
    cnt[ord(alphabet) - 65] += 1

# 4. 이름이 홀수면 중간에 한놈은 한개이고 양옆에 끼는데 그거 표현
center = 0
center_alphabet = ''
alpha = ''

for i in range(26):
    if cnt[i] % 2:  # 5. 카운트 돌면서 홀수개인거 몇개인지 카운트 1개이상이면 바로 째끼라우할라고
        center += 1
        center_alphabet += chr(i + 65)  # 해당 알파벳도 넣어주공
    # 6. 엘스로 해서 할라니께 암것도 없는 놈들도 다같이 기어나와서 0빼고 짝수값을 가지고있는 애들만 넣어줬다
    alpha += chr(i + 65) * (cnt[i] // 2)

if center > 1:
    print("I'm Sorry Hansoo")
else:
    print(alpha + center_alphabet + alpha[::-1])

```



# 신뢰

```python
from collections import deque

for tc in range(1, int(input()) + 1):
    queue = deque(input().split()) # 책에서 본건데,,, 받는 즉시 큐에 넣어주는 방법... 꿀이네..
    N = queue.popleft() #젤 앞에 꺼를 빼버리고

    # 블루와 올린쥐의 위치 (1 <= x <= 100) 와 시간에 대한 초기값 설정
    blue = [1, 0]
    orange = [1, 0]

    result = 0
    while queue:
        robot = queue.popleft()
        button = int(queue.popleft())

        if robot == "B":
            walk = abs(blue[0] - button)
            # 그 시간동안 움직여서 해당 위치에 있을 수 있는거면 
            # 누르는 것만 더하면 되니까 1을 시간에 더해주고
            # (디폴트 값도 포함 = 그 자리에서 바로 누르기)
            # 시간동안 못움직이고 추가적으로 더 움직여야한다면 
            # 상대방이 움직인 시간을 뺴준 값(걸어서 갈수있으니까)에 누르는거 까지 1
            time = 1 if walk <= blue[1] else walk - blue[1] + 1
            
            # 지금 위치 설정
            blue[0] = button
            # 해당 초만 더할꺼라서 0으로 초기화
            blue[1] = 0 
            # 걸리는 시간 넣어주고
            result += time 
            # 블루에서 걸린시간을 오렌지에 알려준다
            orange[1] += time 

        else:
            walk = abs(orange[0] - button)
            time = 1 if walk <= orange[1] else walk - orange[1] + 1
            orange[0] = button
            orange[1] = 0
            result += time
            blue[1] += time

    print("#{} {}".format(tc, result))
```

