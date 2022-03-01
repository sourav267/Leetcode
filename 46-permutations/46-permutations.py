class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def find_all_permutations(index,nums,ans):
            if index == len(nums):
                ans.append(list(nums))
                
            for i in range(index,len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                find_all_permutations(index+1,nums,ans);
                nums[index], nums[i] = nums[i], nums[index]
                    
        # ds = []
        ans = []
        # freq = [False] * len(nums)
        find_all_permutations(0,nums,ans)
        return ans
            