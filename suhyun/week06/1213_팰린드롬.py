palindrome = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0,
    'E': 0, 'F': 0, 'G': 0, 'H': 0,
    'I': 0, 'J': 0, 'K': 0, 'L': 0,
    'M': 0, 'N': 0, 'O': 0, 'P': 0,
    'Q': 0, 'R': 0, 'S': 0, 'T': 0,
    'U': 0, 'V': 0, 'W': 0, 'X': 0,
    'Y': 0, 'Z': 0,
}


def verification():
    rst = ''
    cnt = 0
    mid = ''
    for k, v in palindrome.items():
        if v == 0:
            continue
        if v % 2 == 0:
            rst += k * (v // 2)
        elif v % 2 and not cnt:
            rst += k * (v // 2)
            mid = k
            cnt = 1
        elif v % 2 and cnt:
            return 'I\'m Sorry Hansoo'
    return rst + mid + rst[::-1]


N = input()
for i in range(len(N)):
    palindrome[N[i]] += 1
result = verification()
print(result)
