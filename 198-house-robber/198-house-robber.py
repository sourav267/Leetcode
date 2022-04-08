class Solution:
    def rob(self, nums: List[int]) -> int:
        temp1 = nums[0]
        temp2 = 0
        for i in range(1,len(nums)):
            pick = nums[i] + temp2
            notpick = temp1
            curr  = max(pick,notpick)
            temp2 = temp1
            temp1 = curr
        return temp1
            
            
            
            
                