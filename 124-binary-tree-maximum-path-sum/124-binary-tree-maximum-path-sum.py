# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -1111
        
        def findMaxSum(root):
            if root is None:return 0
            
            l = max(0,findMaxSum(root.left))
            r = max(0,findMaxSum(root.right))
            self.maxSum  = max(self.maxSum,root.val+l+r)
            
            return max(l,r)+root.val
        
        findMaxSum(root)
        return self.maxSum
            
            
        