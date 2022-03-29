# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def buildHelper(postorder,postS,postE,inorder,inS,inE,inMap):

            if postS > postE or inS > inE:
                return None

            root = TreeNode(postorder[postE])
            inRoot = inMap[root.val]
            numsLeft = inRoot - inS

            root.left = buildHelper(postorder, postS, postS+numsLeft-1,
                                inorder, inS, inRoot-1,
                                inMap)
            root.right = buildHelper(postorder, postS + numsLeft, postE -1,
                               inorder, inRoot + 1, inE,
                               inMap)

            return root
        
        inMap = dict()
        for i, e in enumerate(inorder):
            inMap[e] = i
        
        
        root = buildHelper(postorder,0,len(postorder)-1,
                       inorder,0,len(inorder)-1,
                       inMap)
        return root
        