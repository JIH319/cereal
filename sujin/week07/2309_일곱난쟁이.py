# 아홉 난쟁이 중 찐 일곱 난쟁이를 찾아 오름차순으로 출력
# 찐 일곱난쟁이 키의 합은 100

def comb(idx,height_sum):
    global is_true
    if idx == 7 and height_sum == 100:
        seven_man.sort()
        for e in seven_man:
            print(e)
        is_true = 1
        return 

    if idx == 7:
        return

    for i in range(9):
        if selected[i]:continue
        selected[i] = 1
        seven_man[idx] = height[i]
        comb(idx+1,height_sum+height[i])
        if is_true:return
        selected[i] = 0
        

height = []
for i in range(9):
    height.append(int(input()))
selected = [0] * 9
seven_man = [0]*7
is_true = 0
comb(0,0)
# print(height)
# print(selected)
