# 18222. 투에 모스 문자열

# 0 1 2 3 4 5 6 7
# 0 1 1 0 1 0 0 1 

# t0 = 0 
# t1 = 1
# t2n = 1
# t2n+1 = 1-tn
def solve(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 : # 2n+1 을 뜻함
        return 1- solve(n//2)
    else: # 2n 을 뜻함
        return solve(n//2)

# [ 입력 ]
k = int(input())
solve(k)