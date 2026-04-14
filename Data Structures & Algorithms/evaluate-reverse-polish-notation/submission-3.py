class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n!='+' and n!='-' and n!='*' and n!='/':
                stack.append(int(n))
            elif n == '+':
                a = stack.pop()
                b = stack.pop()
                c = a + b
                stack.append(c)
            elif n == '-':
                a = stack.pop()
                b = stack.pop()
                c = b - a
                stack.append(c)
            elif n == '*':
                a = stack.pop()
                b = stack.pop()
                c = a * b
                stack.append(c)
            elif n == '/':
                a = stack.pop()
                b = stack.pop()
                c = b / a
                stack.append(int(c))
        return stack.pop()