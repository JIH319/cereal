# 4223. 삼성이의 트라우마 극복
# 테스트 케이스의 수 T
T = int(input())
for tc in range(1,T+1):
    # 면접관 수 N
    N = int(input())
    arr = []
    for n in range(N):
        arr.append(n+1)
    # 면접관 정리
    mj = []
    for _ in range(N):
        # 면접관에 더해주쟈.
        mj.append([int(input()), list(input().split()), int(input())])
    # SAMSUNG
    min_sum = 10000
    n = len(arr)
    for i in range(1 << n):
        rst = {'S': 0, 'A': 0, 'M': 0, 'U': 0, 'N': 0, 'G': 0}
        m_sum = 0
        for j in range(n):
            if i & (1 << j):
                for a in mj[j][1]:
                    if not rst.get(a) is None:
                        rst[a] += 1
                m_sum += mj[j][2]
        if rst['S'] >= 2 and rst['A'] and rst['M'] and rst['U'] and rst['N'] and rst['G']:
            if min_sum > m_sum:
                min_sum = m_sum
    if min_sum == 10000:
        min_sum = -1
    print('#{} {}'.format(tc, min_sum))
    # for i in range(N):
    #     for j in range(i + 1, N):
    #         rst = {'S': 0, 'A': 0, 'M': 0, 'U': 0, 'N': 0, 'G': 0}
    #         m_sum = 0
    #         for a in mj[i][1]:
    #             rst[a] += 1
    #         for b in mj[j][1]:
    #             rst[b] += 1
    #         if rst['S'] >= 2 and rst['A'] and rst['M'] and rst['U'] and rst['N'] and rst['G']:
    #             m_sum = mj[i][2] + mj[j][2]
    #             if min_sum > m_sum:
    #                 min_sum = m_sum
    # if min_sum == 10001:
    #     min_sum = -1
    # print('#{} {}'.format(tc, min_sum))
