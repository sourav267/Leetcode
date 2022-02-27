class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def findCombination(i,arr,target,list_of_list,ds):
            if i == len(arr):
                if target == 0:
                    list_of_list.append(ds)
                return
            
            if arr[i] <= target:
                # pick the combination
                findCombination(i,arr,target-arr[i],list_of_list,ds + [arr[i]])
                
            # do not pick the combination
            findCombination(i+1,arr,target,list_of_list,ds)
                
        list_of_list  = []
        ds = []
        findCombination(0,candidates,target,list_of_list,ds)
        return list_of_list
        
        
        