'''
1. X는 맨 처음에 "0"으로 시작한다. 
2. X에서 0을 1로, 1을 0으로 뒤바꾼 문자열 X'을 만든다.
3. X의 뒤에 X'를 붙인 문자열을 X로 다시 정의한다. 
4. 2~3의 과정을 무한히 반복한다.
'''
import sys

def calc(tmp):
    global cnt
    if tmp <= 1:
        cnt += 1
        return
    
    i = 0
    # tmp보다 작은 수 중 가장 큰 2의 배수를 빼준다
    while tmp > 2**i:
        i += 1
    if i == 0:  # tmp가 1이 되었을때
        tmp = 0
    else:
        tmp -= 2**(i-1)
    cnt += 1    # 0에서부터 한번 더 나아갔다고 +1
    
    calc(tmp)
# from collections import deque
# 자연수 k가 주어졌을 때 X의 k번째에는 무슨 문자가 오는지 구하여라.
K = int(sys.stdin.readline())
cnt = 0
calc(K)

if cnt%2:
    print(0)
else:
    print(1)

# import sys
# # from collections import deque
# # 자연수 k가 주어졌을 때 X의 k번째에는 무슨 문자가 오는지 구하여라.
# K = int(sys.stdin.readline())

# tmp = K
# # 맨처음 0으로부터 몇번 나아갔는지 셀 변수
# cnt =  0
# # K번째 수부터 거꾸로 0까지 반복
# while tmp:  
#     i = 0
#     # tmp보다 작은 수 중 가장 큰 2의 배수를 빼준다
#     while tmp > 2**i:
#         i += 1
#     if i == 0:  # tmp가 1이 되었을때
#         tmp = 0
#     else:
#         tmp -= 2**(i-1)

#     cnt += 1    # 0에서부터 한번 더 나아갔다고 +1
    
# if cnt%2:
#     print(0)
# else:
#     print(1)




# import sys
# from collections import deque
# # 자연수 k가 주어졌을 때 X의 k번째에는 무슨 문자가 오는지 구하여라.
# K = int(sys.stdin.readline())

# # condition : K번째 문자를 구하기위해, 0이 될때까지 2-3번 과정 반복
# condition = K-1

# data = deque([0])
# while condition:
#     tmp = deque()
#     for i in range(len(data)):
#         if data[i] == 0:
#             tmp.append(1)
#         else:
#             tmp.append(0)
#     data.extend(tmp)
#     condition //= 2

# print(data)

# print(data[K-1])