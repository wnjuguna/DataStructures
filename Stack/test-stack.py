#!/usr/bin/python3

import unittest
from postfix import toPostfix, solvePostfix
from parenthesis import checkBalance

class StackTestCase(unittest.TestCase):
    def testPostfix(self):
        expr = '((7-4)*2)+2'
        res = toPostfix(expr)
        self.assertEqual(res, '74-2*2+')
    
    def testSolvePostfix(self):
        expr = '((7-4)*2)+2'
        postfix = toPostfix(expr)
        res = solvePostfix(postfix)
        self.assertEqual(res, 8)

    def testParenthesis(self):
        expr = '()'
        res = checkBalance(expr)
        self.assertEqual(res, True)

if __name__ == '__main__':
    unittest.main()

