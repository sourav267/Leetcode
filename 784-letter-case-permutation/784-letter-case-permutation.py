class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        def backtrack(result,n,index,s,path):
            if len(path) == n:
                result.append(path)
                return
                
            if s[index].isalpha():
                backtrack(result,n,index+1,s,path+s[index].lower())
                backtrack(result,n,index+1,s,path+s[index].upper())
            else:
                backtrack(result,n,index+1,s,path+s[index])
        
        result = []
        backtrack(result,len(s),0,s,'')
        return result
                
            
        