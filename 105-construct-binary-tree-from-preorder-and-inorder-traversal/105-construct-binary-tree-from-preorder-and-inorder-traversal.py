# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        
        def buildHelper(preorder,preS,preE,inorder,inS,inE,inMap):

            if preS > preE or inS > inE :
                return None

            root = TreeNode(preorder[preS])
            inRoot = inMap[root.val]
            numsLeft = inRoot - inS

            root.left = buildHelper(preorder,preS+1,preS+numsLeft,
                                    inorder,inS,inRoot-1,
                                    inMap)
            root.right = buildHelper(preorder,preS + numsLeft + 1,preE,
                                     inorder,inRoot + 1,inE,
                                     inMap)

            return root
        
        inMap = dict()
        for i,e in enumerate(inorder):
            inMap[e] = i
            
        root = buildHelper(preorder,0,len(preorder)-1,
                           inorder,0,len(preorder)-1,
                           inMap)
        return root
        