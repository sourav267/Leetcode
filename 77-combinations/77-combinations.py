class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        def backtrack(result,arr,n,k,index):
            if k == 0:
                result.append(arr)
            
            else:
                for i in range(index,n+1):
                    # arr.append(i)
                    backtrack(result,arr+[i],n,k-1,i+1)
                    # arr.pop()
        
        result = []
        backtrack(result,[],n,k,1)
        return result
                
        