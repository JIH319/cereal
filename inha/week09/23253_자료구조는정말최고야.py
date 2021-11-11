import sys
input = sys.stdin.readline

# 책 개수 N개, 책 더미 M개
N, M = map(int, input().split())
# 책을 순번대로 정리 가능한지 나타내는 변수 isTrue
# 가능하면 True, 불가능하면 False
isTrue = True
# 책 더미가 M개 이므로 M번 체크
# 책을 순번대로 정리할 수 있으려면 각 더미에 쌓여있는 책들의
# 순번이 높은 책이 위에 있어야함
for i in range(M):
    # 순서대로 쌓는거 불가능하면 M개의 더미를 다 확인할 필요 X
    if not isTrue:
        break
    # 각 더미의 책들을 쌓을 stack
    stack = []
    # 각 더미의 책 개수
    book_cnt = int(input())
    # 각 더미의 책 순번
    books = list(map(int, input().split()))
    for book in books:
        # 순번이 더 큰 책이 위에 오면 순번대로 책 정리 불가
        if stack and stack[-1] < book:
            isTrue = False
            break
        else:
            stack.append(book)
# 결과 출력
if isTrue:
    print('Yes')
else:
    print('No')
