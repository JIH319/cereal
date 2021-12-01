def solution(dartResult):
    answer = 0
    # 싱글이면 1, 더블이면 2, 트리플이면 3을 딕셔너리를 활용하여 부른다.
    dart_dict = {'S':1,'D':2,'T':3}
    # 해당 값을 stack 에 저장한뒤에 나중에 합해준다.
    stack = []
    i = 0
    while i<len(dartResult):
        # 해당 값이 S D T 인경우,
        if dartResult[i] == 'S' or dartResult[i] == 'D' or dartResult[i] == 'T':
            # 10인 경우에는 10 을 가져와 제곱해주고,
            if dartResult[i-1] =='0' and dartResult[i-2] =='1':
                stack.append(int(dartResult[i-2:i])**dart_dict[dartResult[i]])
            # 그 외의 숫자인 경우는 0~9까지 자기가 알아서 들고와서 제곱해준다.
            else:
                stack.append(int(dartResult[i-1])**dart_dict[dartResult[i]])
        # * (스타상) 이 나왔을 경우,
        elif dartResult[i] =='*':
            # 아직 길이가 1이면 마지막 배열 원소만 *2 를,
            if len(stack)==1:
                stack[-1]*=2
            # 길이가 2이상이면, 마지막과 그 전 원소에 * 2 를 해준다.
            else:
                stack[-1]*=2
                stack[-2]*=2
        # # (아차상) 인 경우, 부호를 반대로 만들어준다.
        elif dartResult[i]=='#':
            stack[-1]*=-1           
        # 모든 경우에 일단 i+1은 해준다. (for 문으로해도되겠넹)
        i+=1
    # 해당 원소 stack의 값을 모두 더해주면 우리가 구하고자 하는 answer 가 된다.
    answer = sum(stack)
    return answer