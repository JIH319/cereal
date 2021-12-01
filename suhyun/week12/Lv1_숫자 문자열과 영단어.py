num_dict = {
    'zero':'0','one':'1','two':'2',
    'three':'3','four':'4','five':'5',
    'six':'6','seven':'7','eight':'8',
    'nine':'9'
}

def solution(s):
    # 문자열이 주어진다면, 그 문자열이 그냥 숫자인경우는 바로넣어주고,
    # 문자가 주어진다면 해당하는 글자를 숫자로 바꿔서 저장해주자.
    answer = ''
    i = 0
    while i < len(s):
        # 숫자일 경우, 바로넣어주고 i를 올리자.
        if '0'<=s[i]<='9':
            answer += s[i]
            i += 1
        else:
            # 문자일 경우, 빈 문자열을 받아주고,
            tmp = ''
            # 숫자가 나오기 전까지나, s 의 길이를 벗어나지 않는다면, while 반복문을 도는데,
            while not '0'<=s[i]<='9' and i< len(s):
                tmp += s[i]
                i += 1
                # num_dict 에서 설정한 키 값에 포함될 경우, break 해주고 answer 에 담아주자.
                if tmp in num_dict.keys():
                    break
            answer += num_dict[tmp]
    # 출력으로 필요한 것은 숫자형, int로 변환해주자.
    answer = int(answer)
    
    return answer