class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first,curr,output,nums):
            # if the combination is done is of size k
            output.append(curr)
            for j in range(first, n):
                if j == first or nums[j] != nums[j-1]:
                    backtrack(j + 1, curr+[nums[j]],output,nums)
        
        output = []
        n = len(nums)
        backtrack(0,[],output,sorted(nums))
        return output
        