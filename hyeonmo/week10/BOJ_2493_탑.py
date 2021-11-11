# 첫째 줄에 탑의 수 N
# 두번째 줄에 탑의 높이가 적힌 값 한줄로 주어짐
# 탑은 오른쪽부터 왼쪽으로 현재 탑보다 더 높은 탑이 어디인지 위치값을 찾아내야한다.
# 위치 값은 1부터 시작한 값을 해당 위치에 넣는다.
# 오큰수,옥상정원 꾸미기와 비슷하게 풀어보자

# 풀이
# for 반복문을 오른쪽에서 왼쪽으로 가는데 결과값은 위치를 출력 해야 하니까
# i를 인덱스 값으로 활용
# stack이 비어있거나 stack의 마지막값 인덱스를 가진 탑과 현재 탑을 비교했을때 현재 탑이 더 작다면
# stack에 해당 인덱스(i)를 push
# stack에 값이 있고 현재 top이 stack의 마지막 값 인덱스를 가진 top보다 크다면
# result에 stack 마지막 인덱스와 동일한 위치에 현재위치 i + 1 을 넣어준다.
N = int(input())
top = list(map(int,input().split()))
result = [0]*N
stack = []
for i in range(N-1,-1,-1):
    while stack and top[i] > top[stack[-1]]:
        result[stack.pop()] = i + 1
    stack.append(i)

print(result)