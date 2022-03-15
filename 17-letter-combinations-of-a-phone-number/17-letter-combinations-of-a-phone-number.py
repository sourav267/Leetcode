class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def solve(digits,n,ans,result,map_arr,index):
            if len(ans) == n and index:
                result.append(ans)
                return
            
            for i in range(index,n):
                value = map_arr[int(digits[i])]
                for c in value:
                    solve(digits,n,ans+c,result,map_arr,index+1)
                return ans
                    
        result = []
        map_arr = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        if len(digits) == 0: return []
        if len(digits) == 1:
            return list(map_arr[int(digits)])
        solve(digits,len(digits),"",result,map_arr,0)
        return result
            