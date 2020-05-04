#!/usr/bin/python3

from stack import Stack

def toPostfix(expr):
    pos = 0
    exprList = list(expr)
    postfixList = []
    opStack = Stack()
    precedence = {'-': 1, '+':2, '*':3, '/':4, '(':5}
    while pos < len(exprList):
        if exprList[pos] == '(':
            opStack.push(exprList[pos])
        elif exprList[pos] in '*+-/':
            if opStack.isEmpty():
                    opStack.push(exprList[pos])
            else:
                if (precedence[opStack.peek()] > precedence[exprList[pos]]) \
                        and opStack.peek() in '*+-/':
                    postfixList.append(opStack.pop())
                    opStack.push(exprList[pos])
                else:
                    opStack.push(exprList[pos])
        elif exprList[pos] == ')':
            while not opStack.isEmpty():
                if opStack.peek() == '(':
                    opStack.pop()
                    break
                else:
                    postfixList.append(opStack.pop())
        else:
            postfixList.append(exprList[pos])
        pos = pos + 1
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    
    return "".join(postfixList)

def doMath(op1, op2, operator):
    if operator == '+':
        ans = op1 + op2
    elif operator == '-':
        ans = op1 - op2
    elif operator == '*':
        ans = op1 * op2
    elif operator == '/':
        ans = op1 / op2
    return ans

def solvePostfix(expr):
    exprList = list(expr)
    operandStack = Stack()
    pos = 0
    while pos < len(exprList):
        if exprList[pos] in '*-+/':
            # pop 2 operands calculate push back to stack
            op2 = operandStack.pop()
            op1 = operandStack.pop()
            ans = doMath(op1, op2, exprList[pos])
            operandStack.push(ans)
        else:
            operandStack.push(int(exprList[pos]))
        pos = pos + 1
    return ans

if __name__ == '__main__':
    expr = '((7-4)*2)+2'
    postfix = toPostfix(expr)
    print("Infix: %s -> Postfix: %s" %(expr, postfix))
    print("Result: %s" %(solvePostfix(postfix)))
