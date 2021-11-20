# 6603. 로또
```python
def lotto(start, depth):
    if depth == 6:
        print(*comb)
        return
    for i in range(start, len(data)):
        comb[depth] = data[i]
        lotto(i+1, depth+1)


comb = [0]*6
while True:
    data = list(map(int,input().split()))
    if data[0] == 0:
        break

    data = data[1:]
    lotto(0, 0)
    print()

```



# 11399. ATM

```python
_ = int(input())
people = list(map(int, input().split()))

s_people = sorted(people)
sum_p = 0
acc = 0

for i in s_people:
    sum_p += acc + i
    acc += i

print(sum_p)
```



# 16198. 에너지 모으기

### del / insert 쓴 버전
```python
# x 번째 에너지 구슬 하나 고름 (첫번째, 마지막 x)
# x 번째 에너지 구슬 제거
# x-1 * x+1 에너지 모음
# n을 1 감소
import sys
input = sys.stdin.readline

def energy(my_energy):
    global answer
    if len(W) == 2:
        answer = max(answer, my_energy)
        return

    for i in range(1, len(W)-1):
        my_energy += (W[i-1]*W[i+1])
        temp = W[i]
        del W[i]
        energy(my_energy)
        W.insert(i, temp)
        my_energy -= (W[i-1]*W[i+1])


N = int(input())
W = list(map(int, input().split()))
answer = 0
energy(0)
print(answer)
```

### 슬라이싱 쓴 버전
``` python
import sys
input = sys.stdin.readline


def energy(arr):
    if len(W) == 3:
        return arr[0] * arr[2]
    answer = 0
    for i in range(1, len(arr)-1):
        my_energy = arr[i-1]*arr[i+1] + energy(arr[:i] + arr[i+1:])
        answer = max(my_energy, answer)
    return answer


N = int(input())
W = list(map(int, input().split()))
print(energy(W))
```



# 13305. 주유소

```python
N = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

# 일단 제일 왼쪽도시에서 다음 도시까지의 기름은 무조건 넣어야함
price = oil[0] * road[0]
now_cost = oil[0]
# 그리디 알고리즘 이므로 모든 경우의 수 따져서는 안 됨
# 이전 오일 가격이랑 지금 방문할 도시의 오일 가격을 서로 비교하며 싼 오일 가격으로 업데이트
# 5, 2, 4 1 일 경우... 두번째 도시 방문할 때까지 제일 싼 가격은 5..
# 세번째 도시 방문시, 제일 싼가격은 2.. 업데이트
# 네번째 도시 방문시 역시 싼 가격 2
# 이전 도시에서 네번째 도시 방문할 때까지의 기름을 채웠다고 가정해서 + 제일 싼 가격 * 도로길이
# x번째 도시에서 x+1번째 도시로 가는 도로는 road 배열의 x번 째에 위치함을 기억!
for i in range(1, N-1):
    if now_cost > oil[i]:
        now_cost = oil[i]
        price += now_cost * road[i]
    else:
        price += now_cost * road[i]

print(price)
```



# 1931. 회의실 배정

```python
import sys
input = sys.stdin.readline
# 활동 선택 문제 -> 종료시간을 기준으로 정렬
n = int(input())
meeting = []
for _ in range(n):
    meeting.append(tuple(map(int, input().split())))

# 끝나는 시간이 똑같을 경우 시작 시간이 빠를 것을 선택할 수 있도록
# (2,2) (1,2) 일때 (1,2) (2,2) 일 경우가 될 수 있기 때문에
# key에 튜플로 여러 인자를 주면 인자 순서대로 정렬
meeting.sort(key=lambda x: (x[1], x[0]))

answer = 1
end_time = meeting[0][1]
for i in range(1, n):
    if end_time <= meeting[i][0]:
        answer += 1
        end_time = meeting[i][1]

print(answer)
```


# 1783. 병든 나이트
```python
N, M = map(int, input().split())

# 세로가 1이면 무조건 한칸밖에 못감
if N == 1:
    print(1)

# 세로가 2이면 갈수 있는 방법이 2가지밖에 없음 -> 이동횟수 4번이상이면 안됨 (3칸까지 방문 가능)
elif N == 2:
    print(min(4, (M+1)//2))

# 가로가 7이상이어야지만 이동횟수 4번이상 가능.
# 그 전에는 1칸씩 자기 길이만큼 이동하거나 어떻게든 3번이하로 이동하는 경우밖에 없음
elif M < 7:
    print(min(4, M))

# 이외에는 가로 길이 7까지는 모든 방법을 다 사용해서 방문하는 5칸 + 7 초과부터는 1칸씩 계속 방문 가능
else:
    print(M-7+5)
```

