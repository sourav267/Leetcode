class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def find_all(index,arr,n,sub_set,ds):
            ds.append(sub_set)
            for j in range(index,n):
                if j > index and arr[j] == arr[j-1]: continue
                find_all(j+1,arr,n,sub_set+[arr[j]],ds)
        ds = []
        find_all(0,sorted(nums),len(nums),[],ds)
        return ds
        