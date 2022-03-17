class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for x in s:
            # print(stack1, stack2, result)
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
        return stack.pop()
                    
                    
                
        