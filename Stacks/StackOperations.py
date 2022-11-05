from collections import deque

class stackOperations:

    def __init__(self):
        self.stack = deque()

    # to push the data inside the stack
    def pushData(self,val):
        self.stack.append(val)
        return self.stack

    # It only returns the top most element but doesnot delete it. Unlike pop method which also delete element
    def peekData(self):
        return self.stack[-1]

    # check if stack is empty or not
    def is_empty(self):
        return len(self.stack) == 0

    # to pop out the element from the stack. It also deletes that element
    def popData(self):
        if self.is_empty():
            return "Stack is already empty"
        return self.stack.pop()

    # check the length of the stack
    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    #Push Data
    val = 5
    stack_ops = stackOperations()
    print(stack_ops.pushData(val))

    # Pop Data
    print(stack_ops.popData())
    print(stack_ops.popData())
    # # peek data
    # stack_ops.pushData(val)
    # print(stack_ops.peekData())

    # # is Empty
    # print(stack_ops.is_empty())

    # # size of stack
    # print(stack_ops.size())