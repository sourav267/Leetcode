class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p1=None
        p2=None
        arr=[]
        c=False
        for i in range(len(nums)):
            z=target-nums[i]
            for j in range(len(nums)):
                if z==nums[j] and i!=j:
                    p1=i
                    p2=j
                    c=True
                    break
            if c:
                break
        arr.append(p1)
        arr.append(p2)
        return arr
        