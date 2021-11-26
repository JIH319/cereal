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
