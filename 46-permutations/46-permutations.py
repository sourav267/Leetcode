class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def find_all_permutations(nums,ds,ans,freq):
            if len(ds) == len(nums):
                ans.append(list(ds))
            
            for i in range(len(nums)):
                if not(freq[i]):
                    freq[i] = True
                    ds.append(nums[i])
                    find_all_permutations(nums,ds,ans,freq)
                    ds.pop()
                    freq[i] = False
                    
        ds = []
        ans = []
        freq = [False] * len(nums)
        find_all_permutations(nums,ds,ans,freq)
        return ans
            