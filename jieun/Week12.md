# 숫자 문자열과 단어
```python
num_dict = {'zero': '0', 'one': '1', 'two': '2', 'three':'3', 'four': '4', 'five': '5', 'six': '6', 'seven':'7', 'eight':'8', 'nine':'9'}
def solution(s):
    for k, v in num_dict.items():
        s = s.replace(k, v)
    return int(s)
```

# 비밀지도
```python
# 비트연산자를 사용했고, bin 함수를 이용해 이진수로 바꿔준 뒤, zfill로 앞 부분에 0을 채워줌
# replace로 1은 '#', 0은 공백으로 바꿔주었다. 파이썬 내장함수로 손쉽게 풀리는 문제였다.

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(bin(arr1[i] | arr2[i])[2:].zfill(n).replace('1','#').replace('0',' '))
    return answer
 ```
