# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def findAns(root):
            if not root: return 0
            l = findAns(root.left)
            
            r = findAns(root.right)
            self.diameter =  max(self.diameter,l+r)
            return 1 + max(l,r)
        
        self.diameter = 0
        findAns(root)
        return self.diameter