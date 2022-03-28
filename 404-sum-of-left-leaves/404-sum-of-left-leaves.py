# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue=[root]
        suml = 0
        while queue:
            node = queue.pop(0)
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
            
            if node.left is not None and node.left.left is None and node.left.right is None:
                suml += node.left.val
        
        return suml
            
                    
                
        