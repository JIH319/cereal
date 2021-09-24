# 회원의 나이와 이름이 가입한 순서대로 주어진다.
# 회원들의 나이가 증가하는 순으로 출력하자
# 나이가 같으면 먼저 가입한사람을 출력하자
# 왼쪽부터 오른쪽으로 이동하면서 작은값을 왼쪽으로 정렬

from sys import stdin

members = []
N = int(stdin.readline())
for i in range(N):
    age,name=stdin.readline().split()
    members.append([int(age),name])

members.sort(key=lambda x:(x[0]))
for i in members:

    print(*i)

