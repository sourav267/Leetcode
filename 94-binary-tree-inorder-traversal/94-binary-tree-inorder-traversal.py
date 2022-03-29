# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root
        pre  = TreeNode()
        while curr is not None:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right is not None:
                    pre = pre.right
                
                pre.right = curr
                temp = curr
                curr = curr.left
                temp.left = None
        
        return res
                    
                
        # res, stack = [], []
        # while True:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     if not stack:
        #         return res
        #     node = stack.pop()
        #     res.append(node.val)
        #     root = node.right
        # return res
        