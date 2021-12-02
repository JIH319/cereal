# 풀이 방법
# 배열 arr1,arr2의 10진수를 비트연산자 or로 합친고, bin()으로 묶어준다.
# 0b11100 형태로 나오기 때문에 슬라이싱으로 [:2]부터 가져온다.
# for 문으로 하나씩 합치는것이기 때문에 ans에 더한다.
# 이 때, n개의 갯수에 맞춰 이진수 형태로 만들기 위해 "0" X (n자리수 - 현재 숫자의 자리수)를 해준다.
# 그리고 append 할 때, replace 함수로 1을 #으로, 0을 " " 빈칸으로 바꾼다.

def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        bin_str = bin(arr1[i] | arr2[i])[2:]
        ans.append(("0" * (n - len(bin_str)) + bin_str).replace("1", "#").replace("0", " "))

    return ans
