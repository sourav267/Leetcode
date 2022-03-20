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
        l = 0
        while q:
            level_count = len(q)
            curr_list = []
            for x in range(level_count):
                elem = q.popleft() if l % 2 == 0 else q.pop()
                if l % 2 == 0:
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
            l += 1
        return res
        