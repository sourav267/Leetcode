class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def solve(map_arr,n,digits,ans,comb,index):
            if len(comb) == n:
                ans.append(comb)
                # ans.append(''.join(list(comb)))
                return
            for i in range(index,n):
                digit = digits[i]
                for c in map_arr[int(digit)] :
                    # comb.append(c)
                    solve(map_arr,n,digits,ans,comb+c,index+1)
                    # comb = comb[:-1]
                    # print(ans)
                    # comb.pop()
                return ans
        
        
        map_arr = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        n = len(digits)
        comb = ""
        ans = []
        if n == 0: return []
        if n == 1:
            return list(map_arr[int(digits)])
        return(solve(map_arr,n,digits,ans,comb,0))
                    
                    
            
        