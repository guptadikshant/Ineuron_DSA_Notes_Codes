stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

for _ in range(len(stack)):
    print(stack.pop())
    print(stack)