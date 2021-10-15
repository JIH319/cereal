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

