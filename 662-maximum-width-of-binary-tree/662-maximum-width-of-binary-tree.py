# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None: return root
        ans  = 0
        queue = [(root,0)]
        while queue:
            size = len(queue)
            mmin = queue[0][1]
            first = 0
            last = 0
            for i in range(len(queue)):
                id_curr = queue[0][1]-mmin
                node = queue[0][0]
                queue.pop(0)
                if i == 0: first = id_curr
                if i == size-1: last = id_curr
                
                if node.left:
                    queue.append((node.left,id_curr*2+1))
                if node.right:
                    queue.append((node.right,id_curr*2+2))
            
            ans = max(ans,last-first+1)
        return ans
                
                
        
        