# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def findrightview(node,ds,level):
            if node is None:
                return
            if level == len(ds):
                ds.append(node.val)
            findrightview(node.right,ds,level+1)
            findrightview(node.left,ds,level+1)
         
        res = []
        findrightview(root,res,0)
        return res
            
        