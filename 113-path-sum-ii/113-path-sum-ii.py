# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(root,sum_value,targetSum,arr,result):
            if root is None: return False
            
            if root.left is None and root.right is None and sum_value + root.val == targetSum:
                arr.append(root.val)
                result.append(arr)
                return
            dfs(root.left,sum_value+root.val,targetSum,arr + [root.val],result)
            dfs(root.right,sum_value+root.val,targetSum,arr + [root.val],result)
        
        res = []
        dfs(root,0,targetSum,[],res)
        return res
        