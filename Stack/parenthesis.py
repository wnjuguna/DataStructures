#!/usr/bin/python3

import stack

def checkBalance(parenthesis):
    balanced = True
    pos = 0
    parlist = list(parenthesis)
    myStack = stack.Stack()
    while pos < len(parlist) and balanced:
        if parlist[pos] == '(':
            myStack.push(parlist[pos])
        else:
            if myStack.isEmpty():
                balanced = False
            else:
                myStack.pop()
        pos = pos +1
    if myStack.isEmpty() and balanced:
        return True
    else:
        return False

if __name__ == '__main__':
    par = '())'
    print("Balanced -> %s" %(checkBalance(par)))
