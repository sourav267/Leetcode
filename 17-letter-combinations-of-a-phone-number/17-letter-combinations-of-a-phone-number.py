class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map_arr = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        
        ans = ['']
        for d in digits:
            queue = [x+y for x in ans for y in map_arr[int(d)]]
            ans = queue     
        return ans if digits else []
        
        
        # ans = []
        # ans.append("")
        # for i in range(0,len(digits)):
        #     d = int(digits[i])
        #     while len(ans[0]) == i:
        #         t = ans.pop(0)
        #         for c in map_arr[d]:
        #             ans.append(t+c)
        # return ans
                
        
#         def solve(map_arr,n,digits,ans,comb,index):
#             if len(comb) == n:
#                 ans.append(comb)
#                 return
#             for i in range(index,n):
#                 digit = digits[i]
#                 for c in map_arr[int(digit)] :
#                     solve(map_arr,n,digits,ans,comb+c,index+1)
#                 return ans
        
        
#         map_arr = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
#         n = len(digits)
#         comb = ""
#         ans = []
#         if n == 0: return []
#         if n == 1:
#             return list(map_arr[int(digits)])
#         return(solve(map_arr,n,digits,ans,comb,0))
                    
                    
            
        