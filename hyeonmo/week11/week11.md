# 6603. 로또

```python
# 각 입력줄의 첫번쨰값은 k, 이후부터 집합 s에 포함되는 수가 주어진다.
# 여러개의 테스트케이스 이며 입력값이 0일떄 테스트 케이스가 종료된다.

# k개 만큼의 요소를 가진 집합 s를 만드는 모든 경우의 수를 구하여라


def solve(start,n):
    if n == 6:
        print(*s)
        return

    for i in range(start,len(data)):
        if not used[i]:
            used[i] = 1
            s[n] = data[i]

            solve(i,n+1)
            used[i] = 0

while True:
    data = list(map(int,input().split()))
    if len(data) == 1:
        break
    k = data.pop(0)
    used = [0]*len(data)

    s = [0]*6

    solve(0,0)
    print()

```





# 11399. ATM

```python
# 사람수 N , 걸리는 시간 배열 입력값
# 각 사람이 돈을 인출하는데 걸리는시간들의 합의 최솟값을 구하여라
# 그럼 주어진 시간배열을 오름차순으로 정렬하면 끝!

N = int(input())
time = list(map(int,input().split()))

time.sort()
sum_v = 0
result = 0
for i in time:
    sum_v = sum_v + i
    result += sum_v


print(result)

```



# 16198. 에너지 모으기

```python
# N개의 에너지 구슬
# 두번째 입력값은 에너지 구슬의 무게
# 1. 에너지 구슬 하나를 고른다.
# 2. 고른 에너지 구슬을 제거한다.
# 3. 에너지 구슬을 고를때 첫번째와 마지막구슬은 고를수 없다.
# 4. 제거한 에너지 구슬 양옆의 구슬의 에너지를 곱한 값을 result에 저장한다.
# 5. N을 1 감소시키고 처음부터 다시 에너지구슬을 고른다.
# 위의 조건으로 에너지를 구할때 구할수 있는 에너지양의 최대값을 출력하라
# 재귀

def solve(N):
    global sum_v
    global max_v
    if N == 2:
        if sum_v > max_v:
            max_v = sum_v
            return


    for i in range(1,N-1):
        sum_v += data[i-1] * data[i+1]
        x = data.pop(i)
        solve(N-1)
        data.insert(i,x)
        sum_v -= data[i - 1] * data[i + 1]

N = int(input())
data = list(map(int,input().split()))
sum_v = 0
max_v = -1
solve(N)
print(max_v)
```



# 1931. 회의실배정

```python
N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
end = 0
# print(data)
data.sort(key=lambda x:(x[1],x[0]))
# print(data)
for s,e in data:
    if s >= end:
        end = e
        cnt += 1
print(cnt)
```
