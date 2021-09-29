
'''
try:
    num = int(input())
    nums.append(num)
except:
    break

while True:
    try:
        a = sys.stdin.readline().split()
        print(a)
        # bst.insert(int(a))
        # bst.show()
    except:
        break
'''
import sys

sys.stdin = open("hw\week04\input.txt", "r")

def postorder(V):
    if len(tree) > V:
        postorder(2*V)
        postorder(2*V+1)
        if tree[V]: print(tree[V])

# def postorder(V):
#     current = V # 루트부터 시작
#     N = len(data)
#     visited = [0] * len(tree)
    
#     i = 0
#     current = V 
#     while i < N+1:
#         # 왼쪽 서브 트리 점검   
#         # 방문 안한 왼쪽 노드가 있으면 내려가기
#         while 2*current < len(tree) and tree[2*current] and not visited[2*current]:
#             current = 2*current
        
#         # 오른쪽 서브 트리 점검
#         # 방문 안한 오른쪽 노드 있으면 내려가기
#         if 2*current+1 < len(tree) and tree[2*current+1] and not visited[2*current + 1]:
#             current = 2*current + 1
#             continue # 새 노드에 가면 왼쪽 오른쪽 다시 검사

#         # 후위 순회
#         # 방문한적 있는 노드면 부모로 올라가기
#         if visited[current]:
#             current //= 2
#             continue    # 새 노드에 가면 다시 왼 오 검사
#         visited[current] = 1
#         if tree[current]:print(tree[current])
#         i += 1

        
        
        '''
        # 후위
    # 트리의 범위 안, 왼쪽 노드에 값이 있으면 
    while current*2 < len(tree) and tree[current*2]:
        current *= 2    # 왼쪽 노드로 가자

    # 트리의 범위 안, 오른쪽 노드에 값이 있으면 
    if current*2+1 < len(tree) and tree[current*2+1]:
        current = 2 * current + 1    # 오른쪽 노드로 가자
        '''



data = []
for line in sys.stdin:
    data.append(int(line.rstrip()))

# 최악의 경우 편향트리    
# tree = [0] * (2**len(data)-1)
tree = [0]
tree.append(data[0]) # 루트

idx = 1 # 넣고자 하는 데이터의 인덱스

while idx < len(data):
    current = data[idx] # 지금 넣고자하는 데이터
    comp = 1 # 비교할 숫자의 인덱스, 루트부터 비교
    # 전위 순회
    # 비교할 노드가 있냐
    while len(tree) > comp and tree[comp]:
        # 비교하는 노드보다 작으면
        if tree[comp] > current:
            comp *= 2 # 왼쪽으로
        else:
            comp = comp*2 +1 # 오른쪽으로
    while len(tree) < comp + 1:
        tree.append(0)
    tree[comp] = current # 빈노드에 집어넣음
    idx += 1

print(tree)
postorder(1)



