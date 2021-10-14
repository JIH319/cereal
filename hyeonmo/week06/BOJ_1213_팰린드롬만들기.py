name = input()  # 입력
name_dict = {}  # 딕셔너리로 받을예정
odd_check = 0   # 홀수가 몇개인지 체크
result = []     # 결과

# 문자열을 딕셔너리에 담기(갯수 확인용)
for i in name:
    if i in name_dict:
        name_dict[i] += 1
    else:
        name_dict[i] = 1


# 홀수인게 2개 이상이면 회문 아님
# 홀수가 하나뿐인 정상회문이라면 홀수 key를 값 하나 차감하고 따로 저장
# 홀수가 하나뿐일때 그 홀수 키를 결과의 중앙에 다 넣어버리면 틀림(사전순)
# 예) AABBB = ABABA (정답)
# 예) AABBB = BAAAB (중간에 몰면 틀림)

odd_key = ''
for key,value in name_dict.items():

    # 홀수 찾았을때
    if value % 2 == 1:
        odd_check += 1       # 홀수 찾았다고 체크
        name_dict[key] -= 1  # 홀수였던 자리 -1 하고 해당 키가 무엇인지 저장
        odd_key = key

    # 홀수 2번 이상 찾았을때
    if odd_check >= 2:
        print("I'm Sorry Hansoo")
        break

# 정상 회문이라면
if odd_check < 2:
    # "정답이 여러 개일 경우에는 사전순으로 앞서는 것을 출력한다."
    # key 내림차순 정렬(사전순으로 뒤의 값을 먼저 선택하여 result에 넣기위함, 사전순으로 앞서는 알파벳이 result의 맨앞에 위치하게됨)
    name_dict_sort = sorted(name_dict.items(),key=lambda x:x[0],reverse=True)
    for key,value in name_dict_sort:    # input:AABB ## A:2 B:2 -> B:2 A:2 ## BB -> ABBA
        a = value // 2           # 갯수의 절반을 끊어서 반복문 반씩 돌림
        for j in range(a):
            result.insert(0,key) # 앞에 절반 삽입
        for j in range(a):
            result.append(key)   # 뒤에 절반 삽입
    result.insert(len(result)//2,odd_key) # 홀수였던 값을 중간에 하나 삽입

    print(''.join(result))
