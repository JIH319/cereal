import sys
input = sys.stdin.readline

# def min_idx(li):
#     idx = 0
#     min_num = li[0]
#     for i in range(1, len(li)):
#         if min_num > li[i]:
#             min_num = li[i]
#             idx = i
#     return idx
#
#
# N = int(input())
# age = []
# name = []
# for _ in range(N):
#     people = input().split()
#     age.append(int(people[0]))
#     name.append(people[1])
#
# for _ in range(N):
#     idx = min_idx(age)
#     print(age[idx], name[idx])
#     age[idx] = 201

# li = [1, 2, 3, 4, 0, 1, 1]
# print(min_idx(li))


# 10
# 18 j
# 20 k
# 19 i
# 23 a
# 32 b
# 14 c
# 34 d
# 32 e
# 27 f
# 18 g


N = int(input())

people = []
for _ in range(N):
    age, name = input().split()
    people.append((int(age), name))

sort_p = sorted(people, key=lambda x: x[0])
for i in range(N):
    print(sort_p[i][0], sort_p[i][1])