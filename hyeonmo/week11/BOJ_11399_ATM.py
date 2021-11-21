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
