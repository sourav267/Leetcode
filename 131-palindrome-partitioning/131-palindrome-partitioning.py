class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(s):
            if s== s[::-1]:
                return True
            return False
        
        def findAns(s,path,result):
            if not s:
                result.append(path)
                return
            
            for i in range(1,len(s)+1):
                if isPalindrome(s[:i]):     
                    findAns(s[i:],path + [s[:i]],result)
                    
        ans = []
        findAns(s,[],ans)
        return ans
            
                    
        