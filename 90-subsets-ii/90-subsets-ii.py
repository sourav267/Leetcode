class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def find_all(index,arr,n,sub_set,ds):
            ds.append(list(sub_set))
            for j in range(index,n):
                if j > index and arr[j] == arr[j-1]: continue
                sub_set.append(arr[j])
                find_all(j+1,arr,n,sub_set,ds)
                sub_set.pop()
        ds = []
        find_all(0,sorted(nums),len(nums),[],ds)
        return ds
        