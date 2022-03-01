class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def find_all_permutations(index, nums, ans):
            if index == len(nums):
                ans.append(list(nums))

            for i in range(index, len(nums)):
                if nums[index] == nums[i] and i>index:continue
                nums[index], nums[i] = nums[i], nums[index]
                find_all_permutations(index + 1, list(nums), ans)
                # nums[index], nums[i] = nums[i], nums[index]
            
        ans = []
        find_all_permutations(0,sorted(nums),ans)
        return ans
        