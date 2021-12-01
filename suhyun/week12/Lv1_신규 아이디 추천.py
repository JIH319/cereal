def solution(new_id):
    # 1 단계. 대문자를 소문자로 치환
    rst1 = new_id.lower()
    # 2 단계. 사용가능한 문자를 제외하고 제거
    rst2 = ''
    cnt3 = False
    for n in rst1:
        if '0'<=n<='9' or 'a'<=n<='z' or n == '-' or n =='_':
            rst2 += n
            cnt3 = False
        # 3 단계. 마침표가 2번이상 연속된 부분은 하나의 마침표로 치환.
        if n =='.' and not cnt3:
            rst2 += n
            cnt3 = True
    # 4 단계. 양쪽 끝 마침표 제거 (strip 사용)
    rst2 = rst2.strip('.')
    # 5 단계. new_id 가 빈 문자열 일 경우, a 를 대입
    if not rst2:
        rst2 += 'a'
    # 6 단계. new_id 가 16자 이상이라면, 첫 15개 문자를 제외하고 나머지 문자 모두 제거, 마침표일경우 마침표도 제거
    if len(rst2)>=16:
        rst2 = rst2[:15]
    answer = rst2.rstrip('.')
    # 7 단계. new_id 가 2자 이하라면, new_id 의 마지막 문자를 new_id 의 길이가 3이 될때 까지 반복.
    while len(answer)<=2:
        answer += answer[-1]
    return answer

# 아이디 길이는 3자이상 15자 이하
# 아이디는 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표 만 사용가능
# . 는 처음과 끝에 사용할 수 없고 연속으로도 사용 불가
