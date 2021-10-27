# 2003.  수들의 합 2
# N개의 수로 된 수열이 있다. 이 수열의 i번째 수부터 j번째 수 까지의 합이 M이 되는 경우의 수를 구하는
# 프로그램을 작성하시오.


def solve():
    global cnt
    for i in range(N):
        # 시작점 i 번째를 둔다.
        cnt_sum = 0
        for j in range(i, N):
            # cnt_sum 에 그 값을 더해준 후에 조건문을 판별한다.
            cnt_sum += arr[j]
            # 넘어설경우 더 볼필요 없다 break 해준다.
            if cnt_sum > M:
                break
            # 일치한 경우, count 를 올려주고 break 해준다.
            if cnt_sum == M:
                cnt += 1
                break
            # 미 일치시, continue 로 다음 j 번째 수를 더해준다.
            else:
                continue


# 입력
N, M = map(int, input().split())  # N : 수열의 수, M : 구해야하는 경우의 수
arr = list(map(int, input().split()))  # 수열이 가지고 있는 수
# 비트연산으로 구해보자
cnt = 0
solve()
print(cnt)
