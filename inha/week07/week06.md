### [백준/14888] 연산자 끼워넣기

```python
import sys
input = sys.stdin.readline


def cal(op):    # op : 순열이 완성된 연산자 리스트
    n = nums[:] # 숫자 num를 복사
    for i in range(N-1): # 연산자 수 만큼 for문
        if op[i] == 0:
            # 숫자 리스트 n의 i번째와 i+1번째를 i번째 연산자로 계산
            n[i+1] = n[i] + n[i+1]
        elif op[i] == 1:
            n[i+1] = n[i] - n[i+1]
        elif op[i] == 2:
            n[i+1] = n[i] * n[i+1]
        elif op[i] == 3:
            if n[i] < 0:
                n[i+1] = - ((-n[i]) // n[i+1])
            else:
                n[i+1] = n[i] // n[i+1]
    return n[-1]


# 연산자들의 순열을 만들고
# 완성된 순열을 가지고 계산하기
def perm(k):
    global min_v, max_v
    # 순열이 숫자의 개수인 N보다 1작은 N-1이 되었을 때 return
    if k == N-1:
        # 순열이 완성되었으므로 계산
        ans = cal(perm_lst)
        if ans < min_v:
            min_v = ans
        if ans > max_v:
            max_v = ans
        return
    # 순열이 덜 완성되었다면
    else:
        # 연산자가 저장된 리스트를 돌면서
        for i in range(4):
            # operators의 i번째에 추가될 연산자가 있다면
            if operators[i]:
                # 연산자를 의미하는 인덱스 i를 perm_lst에 추가
                perm_lst.append(i)
                # i번째 인덱스가 한개 사용되었으므로 -1 해줌
                operators[i] -= 1
                # 순열의 다음번째에 올 연산자를 구하기 위해 재귀호출
                perm(k+1)
                # i번째 인덱스가 다 사용되었으므로 다시 +1
                operators[i] += 1
                # perm_lst도 원상복귀
                perm_lst.pop()


N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
# 완성된 연사자들의 순열을 저장할 리스트
perm_lst = []
min_v, max_v = 1000000000, -1000000000
perm(0)
print(max_v, min_v, sep='\n')
```



### [SWEA/2112] 보호필름

#### 시간초과 남!

```python
def check(arr): # 성능검사를 통과한 경우 1, 통과하지 못한 경우 0을 반환
    result = 1
    # 열 우선 순회
    for j in range(W):
        order = arr[0][j]
        cnt = 0
        for i in range(D):
            if arr[i][j] == order:
                cnt += 1
                if cnt == K:
                    break
            else:
                cnt = 1
                order = arr[i][j]
        else: result = 0    # 성능통과 못 함
    return result


# 성능 검사 통과하지 못 했다면 약물 투입
def insert(idx, arr, cnt):  # idx: 약물 투입할 행의 인덱스, arr: 성능검사할 필름, cnt: 약물투입한 횟수
    global min_v
    # min_v보다 투입한 횟수가 많으면 return
    if cnt >= min_v:
        return
    # 성능검사 결과 통과 가능하면
    if check(arr):
        if min_v > cnt:
            min_v = cnt
        return
    # 마지막 행까지 약물을 투입해봤을 때 return
    if idx == D:
        return
    # 약물 투입한 행을 약물 투입 후에 다시 복구시키기 위해서 복사해둠
    temp = list(arr[idx])
    # 0: A 약물, 1: B 약물
    # idx 행에 A 약물 투입하거나
    arr[idx] = [0]*W
    insert(idx+1, arr, cnt+1)
    arr[idx] = temp
    # idx 행에 B 약물 투입
    arr[idx] = [1]*W
    insert(idx+1, arr, cnt+1)
    arr[idx] = temp
    # 약물 투입 안 하거나
    insert(idx+1, arr, cnt)


for tc in range(1, int(input())+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    min_v = D
    if not check(film): # 통과하지 못하면
        insert(0, film, 0)  # 약물 투입
    else:   # 한번에 성능 검사 통과하면
        min_v = 0
    print('#{} {}'.format(tc, min_v))
```



