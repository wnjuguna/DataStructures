#!/usr/bin/python3

class Stack:
    def __init__(self):
        self.s= []
        return

    def isEmpty(self):
        if len(self.s) > 0:
            return False
        else:
            return True

    def push(self, item):
        self.s.append(item)
        return

    def pop(self):
        if self.isEmpty():
            return
        else:
            return self.s.pop()

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.s[-1]

if __name__ == '__main__':
    myStack = Stack()
    myStack.push('A')
    myStack.push('B')
    myStack.push('C')
    print("isEmpty -> %s" %(myStack.isEmpty()))
    print("Peek -> %s" %(myStack.peek()))
    print("Pop -> %s"  %(myStack.pop()))
    print("Peek -> %s" %(myStack.peek()))
    print("Pop -> %s"  %(myStack.pop()))
    print("Peek -> %s" %(myStack.peek()))
    print("Pop -> %s"  %(myStack.pop()))
    print("Peek -> %s" %(myStack.peek()))
    print("isEmpty -> %s" %(myStack.isEmpty()))
