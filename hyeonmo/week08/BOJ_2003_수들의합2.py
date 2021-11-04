# N 개의 숫자들 i부터 j까지의 합이 M이 되는 경우의 수를 구하라
# 맨앞 인 i 위치 부터 합해서 M이 넘어가면 i+1 부터 다시 검사
# 시간초과로 pypy에서만 통과
N,M = map(int,input().split())
data = list(map(int,input().split()))
ans = 0

for i in range(N):
    sum_v = 0   # 경우의수 검사 할때마다 0으로 초기화
    for j in range(i,N):
        sum_v += data[j]
        if sum_v == M:   # M이 정확하게 맞아 떨어진다면 경우의 수 +1, break로 다음 경우의수 검사
            ans += 1
            break
        elif sum_v > M:  # 넘어간다면 break
            break

print(ans)




# 투 포인터 알고리즘을 이용하여 python 에서도 통과
# while 조건은 start가 end를 넘어가거나 end가 N보다 같거나 큰경우(넘어가는 경우) 종료
# start와 end가 같은 위치라면 start위치의 값만 sum_v에 할당
# start와 end 가 다른 위치라면 start부터 end까지의 값을 더해서 sum_v에 할당

# start와 end의 합이 M을 넘어버리고 start의 위치가 end보다 앞이라면 start를 1 증가한다.
# 그게 아니라면 계속해서 end를 1씩 증가하여 sum_v를 비교해준다.
'''
N,M = map(int,input().split())
data = list(map(int,input().split()))
ans = 0
start = 0
end = 0
while start <= end and end < N:
    if start == end:
        sum_v = data[start]
    else:
        sum_v = sum(data[start:end+1])
    if sum_v == M:
        ans += 1

    if sum_v > M and start < end:
        start += 1
    else:
        end += 1

print(ans)
'''