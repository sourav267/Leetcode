class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        string_list = list(s)
        stack = []
        for i,char in enumerate(string_list):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    string_list[i] = ''
        while stack:
            string_list[stack.pop()] = ''
        return ''.join(string_list)
                
            
        