class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first,curr,output,k):
            # if the combination is done is of size k
            if len(curr) == k:  
                output.append(curr)
                return
            for j in range(first, n):
                backtrack(j + 1, curr+[nums[j]],output,k)
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack(0,[],output,k)
        return output
        