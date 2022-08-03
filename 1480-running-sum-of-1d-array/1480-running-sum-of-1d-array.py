class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_arr = [nums[0]]
        for i in range(1,len(nums)):
            sum_arr.append(sum_arr[i-1] + nums[i])
        return sum_arr