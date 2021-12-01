def solution(board, moves):
    # 정사각 격자이므로, n 의 길이는 항상 구할 수 있다.
    n = len(board)
    # moves 로 이동시키고, 그게 애니팡~ 이 되버리면 날라가며, 그 갯수를 샌다. 2개가 사라지므로 결과값은 항상 짝수
    # 저장할 배열을 구해주자.
    stack = [0]
    answer = 0
    for move in moves:
        for i in range(n):
            if board[i][move-1]:
                # move 는 1 부터 시작하는 데, 배열은 0부터 시작하니까 -1해주고 시작
                # 기존에 담긴 stack 과 일치하면 +=2 해주면서 pop 만해주고 사용한건 0으로,
                if stack[-1]==board[i][move-1]:
                    stack.pop()
                    answer += 2
                    board[i][move-1] = 0
                    break
                # 그게 아니라면, stack에 넣어주고, 사용한건 0으로
                else:
                    stack.append(board[i][move-1])
                    board[i][move-1] = 0
                    break
    return answer