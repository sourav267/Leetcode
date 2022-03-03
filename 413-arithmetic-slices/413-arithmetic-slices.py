class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        curr =0
        sum1 =0
        if len(nums) < 3:
            return 0
        else:
            for i in range(2,len(nums)):
                if nums[i-1]-nums[i] == nums[i-2]-nums[i-1]:
                    curr +=1
                    sum1 +=curr
                else:
                    curr =0
        # print(curr)
        # print(sum1)
        return sum1
                
        