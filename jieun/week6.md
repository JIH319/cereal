# 1213. 팰린드롬 만들기
```python
def palindrome():
    check = ''
    answer_list = []
    for k, v in munza.items():
        if v % 2:
            if check:
                return 'I\'m Sorry Hansoo'
            check = k
            for _ in range(v//2):
                answer_list.append(k)
        else:
            for _ in range(v//2):
                answer_list.append(k)
    answer_list.sort()
    return ''.join(answer_list) + check + ''.join(answer_list[::-1])


munza = {}

for char in input():
    if char in munza.keys():
        munza[char] += 1
    else:
        munza[char] = 1

print(palindrome())
```
