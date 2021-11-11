n = int(input())
numbers = []
for _ in range(n):
    k = int(input())
    if k == 0:
        numbers.pop()
    else :
        numbers.append(k)
        
print(sum(numbers))