import sys

def palindrome(arr,N):
    arr.sort()     # 문자열 정렬

    # 글자수가 홀수라면 >> 하나만 홀수개수
    if N & 1:
        count = 1
    # 글자수가 짝수라면 >> 모든 문자는 짝수개수
    else:
        count = 0
    i = 0               # 문자열 리스트 인덱스
    cnt = 0             # 홀수 개수의 문자가 나오면 카운팅
    palin = ['A'] * N   # palindrome 만들 리스트
    pidx = 0            # palindrome 인덱스
    # 허용 가능 홀수 개수 넘거나 인덱스가 넘으면 반복 탈출
    while cnt <= count and i+1 < N:
        if arr[i] == arr[i+1]: # 연달아 같은 수면
            palin[pidx],palin[N-1-pidx] = arr[i],arr[i+1]
            pidx += 1
            i += 2
        else:
            palin[N//2] = arr[i]
            i += 1
            cnt += 1
    # 팰린드롬 불가능
    if cnt > count:
        print("I'm Sorry Hansoo")
        return
    # 글자수 홀수, 마지막 글자가 회문 중간글자일때
    elif cnt < count:
        palin[pidx] = arr[-1]
    print(''.join(palin))

    ## 딕셔너리 카운팅할까말까~~


# data: 임한수의 영어이름 / len(data) <= 50 >> 팰린드롬 만들기
data = list(sys.stdin.readline().rstrip())
N = len(data)
palindrome(data, N)