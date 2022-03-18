# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,sum_value,targetSum):
            if root is None: return False
            if root.left is None and root.right is None and sum_value + root.val == targetSum:
                return True
            return dfs(root.left,sum_value+root.val,targetSum) or dfs(root.right,sum_value+root.val,targetSum)
        ans = dfs(root,0,targetSum)
        return ans
            
        