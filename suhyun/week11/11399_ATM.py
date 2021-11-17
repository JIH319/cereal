# 11399. ATM
# 인하은행
N = int(input())  # 사람의 수
arr = list(map(int, input().split()))[:N]
# 최소 값은 오름차순 배열일 때 가능하다.
arr.sort()
# 최종 합
result = 0
# 더해지는 시간
money_time = 0
for i in range(N):
    money_time += arr[i]
    result += money_time
print(result)
