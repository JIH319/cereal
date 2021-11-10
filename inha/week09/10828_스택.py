import sys
input = sys.stdin.readline


# Stack 클래스를 만들어서 클래스의 메서드를 만들어주었다.
class Stack:
    # Stack 클래스를 생성하면 빈 리스트가 생성됨
    def __init__(self):
        self.arr = []

    # value 값을 리스트에 삽입
    def push(self, value):
        self.arr.append(value)

    # stack의 마지막 요소 꺼내기
    def pop(self):
        if self.arr:
            return self.arr.pop()
        else:
            return -1

    # stack의 크기 구하기
    def size(self):
        return len(self.arr)
    
    # stack이 비어있는지 확인
    def empty(self):
        if self.arr:
            return 0
        else:
            return 1
    
    # stack 제일 위에 있는 요소 값 찾기
    def top(self):
        if self.arr:
            return self.arr[-1]
        else:
            return -1


N = int(input())
stack = Stack()

for _ in range(N):
    command = list(input().split())
    if command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        print(stack.pop())
    elif command[0] == 'size':
        print(stack.size())
    elif command[0] == 'empty':
        print(stack.empty())
    elif command[0] == 'top':
        print(stack.top())
