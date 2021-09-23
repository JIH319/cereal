# 10814_나이 순 정렬
# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로,
# 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오

import sys

input = sys.stdin.readline
# [입력]
# 첫째 줄에 온라인 저지회원의 수 N이 주어진다.(1<=N<=100,000)
N = int(input())
# 둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다.
# 나이는 1보다 크거나 같으며,200보다 작거나 같은 정수이고,이름은알파벳 대소문자로 이루어져있고,
# 길이가 100보다 작거나 같은 문자열이다.
oja = []
for n in range(N):
    # 온라인 저지 회원의 수 (Online Judge Account)
    #     oja.append([n]+input().split())
    #     oja[n][1] = int(oja[n][1])
    #     for j in range(n):
    #         if oja[n][1]<oja[j][1]:
    #             oja[n],oja[j]=oja[j],oja[n]
    #         elif oja[n][1]==oja[j][1]:
    #             if oja[n][0]<oja[j][0]:
    #                 oja[n], oja[j] = oja[j], oja[n]
    # for i in range(N):
    #     print('{} {}'.format(oja[i][1],oja[i][2]))
    oja.append(input().split())
    oja[n][0] = int(oja[n][0])
oja.sort(key=lambda x: x[0])
for i in range(N):
    print('{} {}'.format(oja[i][0], oja[i][1]))
