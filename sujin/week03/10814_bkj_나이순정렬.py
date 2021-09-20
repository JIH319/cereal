'''
import sys
N = int(sys.stdin.readline())
data = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    data.append((age, name))
for j in range(N-1,0,-1):
    for k in range(0,j):
        if data[k][0] > data[k+1][0]:
            data[k],data[k+1] = data[k+1],data[k]
for e in data:
    print(' '.join(e))
'''

'''
import sys
N = int(sys.stdin.readline())
data = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    data.append((age, name))
data.sort(key=lambda x:x[0])
for e in data:
    print(' '.join(e))
'''
'''

import sys
N = int(sys.stdin.readline())
data = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    # 첫번째 원소
    if not data:
        data.append((age, name))
        continue
    # 리스트 원소 존재시 비교후 삽입
    for i in range(len(data)):
        if data[i][0] > age:
            data.insert(i, (age, name))
            break
    # 리스트 가장 마지막수의 같거나 그보다 클 경우
    else:
        data.append((age, name))
for e in data:
    print(' '.join(e))
'''

'''
import sys
N = int(sys.stdin.readline())
data = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    data.append((age, name))
for j in range(N-1,0,-1):
    for k in range(0,j):
        if data[k][0] > data[k+1][0]:
            data[k],data[k+1] = data[k+1],data[k]
for e in data:
    print(' '.join(e))
'''

import sys
N = int(sys.stdin.readline())
data = {}
age_list = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    # 나이만 담는 리스트 생성(중복X)
    if age not in age_list:
        age_list.append(age)
    # 나이를 키로 하는 딕셔너리 
    if age in data:
        data[age].append(name)
    else:
        data[age] = [name]
# 가장 작은 나이부터 나이목록에서 추출
while age_list:
    temp = min(age_list)
    temp_list = data[temp]
    # 해당 나이의 이름을 순서대로 출력
    for e in temp_list:
        print('{} {}'.format(temp, e))
    age_list.remove(temp)