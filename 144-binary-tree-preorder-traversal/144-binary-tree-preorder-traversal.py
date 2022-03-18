# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node, stack, ans = root, [], []
        while node is not None:
            ans.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            node = node.left
            if node == None and stack != []:
                node = stack.pop()
        return ans
            
            
            
             