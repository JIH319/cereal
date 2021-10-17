# 2112. 보호필름
```python3
def k_check(): # K개 연속 체크 함수
    for j in range(W):
        first_char = film[0][j]
        check = 0
        for i in range(D):
            if first_char == film[i][j]:
                check += 1
            else:
                first_char = film[i][j]
                check = 1
            if check >= K: # 한 열에 연속한 특성이 K보다 크면 더 볼 것 없음
                break
        if check < K: # 한 열에 연속한 특성이 K개보다 작으면 더 볼 것도 없음
            return False
    return True


def solve(cnt, change_idx): # 재귀를 이용한 조합
    global min_cnt

    if k_check(): # 함수 실행하자마자 연속 K개가 있는지 체크 (약품을 안 발라줘도 될 경우를 위한 가지치기)
        min_cnt = min(cnt, min_cnt)
        return

    if cnt >= min_cnt: # 가지치기
        return

    for i in range(change_idx+1, D):
        origin_film = film[i][:]
        for j in range(W): # 특성 변경
            film[i][j] = 1
        solve(cnt+1, i)

        for j in range(W): # 특성 변경
            film[i][j] = 0
        solve(cnt+1, i)

        for j in range(W): # 원상 복귀
            film[i][j] = origin_film[j]


for tc in range(1, int(input())+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    min_cnt = D+1
    solve(0, -1)
    print('#{} {}'.format(tc, min_cnt))
```


# 14888. 연산자 끼워넣기
```python3
n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_v = int(1e9)
max_v = -int(1e9)

def solution(i, val):
    global min_v, max_v, add, sub, mul, div
    
    if i == n:
        min_v = min(min_v, val)
        max_v = max(max_v, val)
    
    else:
        if add > 0 :
            add -= 1
            solution(i+1, val + data[i])
            add += 1
            
        if sub > 0 :
            sub -= 1
            solution(i+1, val - data[i])
            sub += 1
            
        if mul > 0 :
            mul -= 1
            solution(i+1, val * data[i])
            mul += 1
            
        if div > 0 :
            div -= 1
            solution(i+1, int(val / data[i]))
            div += 1

solution(1, data[0])
print(max_v)
print(min_v)
```
