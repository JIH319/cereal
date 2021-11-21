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