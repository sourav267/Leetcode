class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def findAllCombination(k,n,start,ans,comb):
            if len(comb) == k and n == 0:
                ans.append(comb)
                return
            
            for i in range(start,10):
                findAllCombination(k,n-i,i+1,ans,comb+[i])
        
        ans = []
        findAllCombination(k,n,1,ans,[])
        return ans
            
        
            
        
        