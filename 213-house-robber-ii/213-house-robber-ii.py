class Solution:
    def rob(self, nums: List[int]) -> int:

        def findMax(arr):
            prev1, prev2 = arr[0], 0
            for i in range(1,len(arr)):
                pick = arr[i] + prev2
                not_pick = prev1
                curr = max(pick,not_pick)
                prev2 = prev1
                prev1 = curr
            
            return prev1
        if len(nums)==1:
            return nums[0]
        return max(findMax(nums[1:]),findMax(nums[:-1]))
        
            
        