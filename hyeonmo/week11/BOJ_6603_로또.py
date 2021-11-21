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
