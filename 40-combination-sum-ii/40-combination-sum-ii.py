class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def findCombination(index, arr, target, list_of_list, ds):
            if target == 0:
                list_of_list.append(list(ds))
                return

            for i in range(index, len(arr)):
                if i > index and arr[i] == arr[i - 1]:
                    continue

                if arr[i] > target:
                    break
                ds.append(arr[i])
                findCombination(i + 1, arr, target - arr[i], list_of_list, ds)
                ds.pop()

        list_of_list = []
        ds = []
        findCombination(0, sorted(candidates), target, list_of_list, ds)
        return list_of_list
                
        