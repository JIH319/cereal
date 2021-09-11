import sys

sys.stdin = open('input.txt')

blinddate = 11 * 60 * 24 + 11 * 60 + 11

for tc in range(int(input())):
    # d일 h시 m분
    d, h, m = map(int, input().split())
    dumped = d * 60 * 24 + h * 60 + m
    result = dumped - blinddate

    if result < 0:
        result = -1

    print('#{} {}'.format(tc+1, result))
