'''
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

'''
## 시간초과남 ;; ##
# class Stack():
#     def __init__(self,N):
#         self.arr = [0] * N
#         self.top_idx = -1

#     def push(self, val):
#         self.top_idx += 1
#         self.arr[self.top_idx] = val

    
#     def pop(self):
#         if self.top_idx < 0:
#             return -1
#         else:
#             self.top_idx -= 1
#             return self.arr[self.top_idx+1]

#     def size(self):
#         return self.top_idx+1

#     def empty(self):
#         # 비어있지 않으면 0, 
#         if self.top_idx >= 0:
#             return 0
#         # 비어있으면 1
#         else:
#             return 1
#     def top(self):
#         # 비어있지 않으면 top 값
#         if self.top_idx >= 0:
#             return self.arr[self.top_idx]
#         # 비어있으면 -1
#         else:
#             return -1
# # N : 반복의 횟수
# N = int(input())
# stack = Stack(N)
# for i in range(N): 
#     tmp = input().split()
#     if tmp[0] == 'push':
#         stack.push(int(tmp[1]))
#     elif tmp[0] == 'pop':
#         print(stack.pop())
#     elif tmp[0] == 'size':
#         print(stack.size())
#     elif tmp[0] == 'empty':
#         print(stack.empty())
#     else:
#         print(stack.top())

## 시간초과;; ##
N = int(input())
stack = [0] * N
top_idx = -1
for i in range(N): 
    tmp = input().split()
    if tmp[0] == 'push':
        top_idx += 1
        stack[top_idx] = int(tmp[1])

    elif tmp[0] == 'pop':
        if top_idx >= 0 :
            print(stack[top_idx])
            top_idx -= 1
        else:
            print(-1)

    elif tmp[0] == 'size':
       
        print(top_idx+1)
       
    elif tmp[0] == 'empty':
        if top_idx >= 0 :
            print(0)
        else:
            print(1)

    else:
        if top_idx >= 0:
            print(stack[top_idx])
        else:
            print(-1)