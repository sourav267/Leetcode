class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        z=0
        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '{':
                stack.append('}')
            elif i == '[':
                stack.append(']')
            elif stack == [] or stack.pop() != i:
                return False
        if stack == []:return True
        else: return False