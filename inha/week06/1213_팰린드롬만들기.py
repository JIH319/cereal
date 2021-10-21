import sys

input = sys.stdin.readline
lst = list(input().strip())
dic = {}

for k in lst:
    if k in dic.keys():
        dic[k] += 1
    else:
        dic[k] = 1

odd, even = 0, 0
for v in dic.values():
    if v%2:
        odd += 1
    else:
        even += 1

# 1. 홀수 개인 문자가 없고 짝수 개인 문자만 있는 경우
# 2. 홀수 개인 문자가 1개 있고 짝수 개인 문자가 있는 경우
# 3. 홀수 한개인 문자만 있는 경우
if odd > 1: # 홀수가 2개이상이면 회문 만들 수 없음
    print("I'm Sorry Hansoo")
else:
    keys = list(dic.keys())
    keys.sort() # 사전순으로 정렬
    length = len(lst)  # 문자열 길이
    pal = [''] * length
    i, temp = 0, 0
    for k in keys:
        if dic[k] > 1:
            if dic[k] % 2:
                temp = k
            for j in range(dic[k] // 2):
                pal[0 + i] = k
                pal[length - 1 - i] = k
                i += 1
        else:  # 홀수 개 문자
            temp = k
    if temp:  # temp이 0이 아니면
        pal.insert(length // 2, temp)
    for ans in pal:
        print(ans, end='')