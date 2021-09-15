N = int(input())
money = []
for _ in range(N):
    M = int(input())
    if M:
        money.append(M)
    else:
        money.pop()

result = sum(money)
print(result)