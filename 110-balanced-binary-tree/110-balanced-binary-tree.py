# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def findAns(root):
            if not root: return 0
            l = findAns(root.left)
            if l== -1:return -1
            
            r = findAns(root.right)
            if r == -1:return -1
            
            if (abs(l-r)>1): return -1
            return max(l,r)+1
        
        ans = findAns(root) != -1
        return ans
        