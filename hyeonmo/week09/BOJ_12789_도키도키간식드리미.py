# 번호표 순서가 엉망인 입력값 한줄이 들어온다.
# 배열 하나를 더 이용해서 현재 나가야 할 번호보다 높으면 새로 만든 배열에 이동시킨다.
# 낮은 번호먼저 계속 보내서 더이상 보내야 할 숫자가 없으면 성공!

N = int(input())
# 검사하기 쉽게 정수로 받는다.
input_list = list(map(int,input().split()))
spare_list = []
i = 1
while True:
    if input_list:
        # input_list의 맨앞 번호가 나갈 차례랑 일치한다면 보내고 i는 +1
        if input_list[0] == i:
            input_list.pop(0)
            i+=1
        # 나갈 차례보다 맨앞 번호가 더 크다면
        elif input_list[0] > i:
            # spare로 보낸값이 있다면 보낸 값부터 검사해보기
            if spare_list:
                if spare_list[-1] == i:
                    spare_list.pop()
                    i += 1
                    continue    # spare에 있는게 보낼 차례랑 일치한다면 보내고 continue
            # spare가 비어있거나 보낼 차례가 아니라면 input_list의 값을 spare로 보내기
            pop_data = input_list.pop(0)
            spare_list.append(pop_data)

    # input_list가 비어있고 spare에 값이 있다면 검사
    elif spare_list:
        if spare_list[-1] == i:
            spare_list.pop()
            i += 1
        # spare의 끝값이 나갈수 없다면 실패
        else:
            print('Sad')
            break
    # 모든 번호가 나가서 배열이 모두 비었다면 성공!
    else:
        print('Nice')
        break




