from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print(stack)

for _ in range(len(stack)):
    print(stack.pop())
    print(stack)