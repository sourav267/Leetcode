# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        l_to_r = True
        while q:
            level_count = len(q)
            curr_list = []
            for x in range(level_count):
                elem = q.popleft() if l_to_r else q.pop()
                if l_to_r :
                    if elem.left:
                        q.append(elem.left)
                    if elem.right:
                        q.append(elem.right)
                else:
                    if elem.right:
                        q.appendleft(elem.right)
                    if elem.left:
                        q.appendleft(elem.left)
                curr_list.append(elem.val)
            res.append(curr_list)
            l_to_r = not l_to_r
        return res
        