# N : 교과서의 수
# M : 교과서 더미의 수
# 둘째 줄부터 M*2 줄에 걸쳐 입력값 주어짐
# 교과서 더미의 수 만큼 배열을 만들어서 하나의 배열에 합치기(2차원배열)

# 각 더미를 순서대로 순회하는게 아니다!!
# 하나씩 뽑아서 뽑은것들끼리 비교, 가장 작은값을 result 배열에 넣자
# 그 다음은 result의 마지막요소와 비교해서 result가 더 크다면 No

# 구현을 못했다...
# 시간이 남는다면 위의 아이디어로 다시 풀어보자

# 질문검색을 참고해서 내림차순으로 정렬하면 된다는 아이디어를 얻고 풀어보았다.
# 입력값을 받고 정렬하여 검사하면 시간초과
# sys 모듈을 쓰지 않으면 시간초과
# 입력을 받고나서 바로 검사하여 확인해야한다.

import sys

N,M = map(int,sys.stdin.readline().split())
for i in range(M):
    _ = sys.stdin.readline() # 책의 개수는 필요없기에 변수에 할당하지 않는다.
    book = list(map(int,sys.stdin.readline().split()))
    # 내림차순값을 sort_data 에 할당하고 원본과 비교
    sort_data = sorted(book,reverse=True)
    if book != sort_data:
        print('No')
        break
else:
    print('Yes')
