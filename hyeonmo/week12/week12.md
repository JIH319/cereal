# 신규아이디 추천

```python
input_data = input()
id = []
# 1단계
input_data = input_data.lower()


# 2단계 3단계
for x in range(len(input_data)):
    if input_data[x].isalpha():
        id.append(input_data[x])

    elif input_data[x].isdigit():
        id.append(input_data[x])
    elif input_data[x] == '-' or input_data[x] == '_':
        id.append(input_data[x])

    # 3단계계
    elif input_data[x] == '.':
        if id and id[-1] == '.':
            continue
        else:
            id.append((input_data[x]))

# 4단계
if id and id[0] == '.':
    id.pop(0)
if id and id[-1] == '.':
    id.pop()
# 5단계
if id == []:
    id.append('a')
# 6단계
if len(id) >= 16:
    id = id[:15]
    if id[-1] == '.':
        id.pop()
# 7단계
if len(id) <= 2:
    f = len(id)
    while f != 3:
        id.append(id[-1])
        f += 1
result = ''.join(id)
print(result)

```

