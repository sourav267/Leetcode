class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(ans,string,openb,closeb,n):
            if len(string) == 2*n:
                ans.append(string)
                return 
            
            if openb < n:
                backtrack(ans,string+"(",openb+1,closeb,n)
        
            if closeb < openb:
                backtrack(ans,string+")",openb,closeb+1,n)
        ans=[] 
        backtrack(ans,"",0,0,n)
        return ans
        
                
                
            
            
                
        