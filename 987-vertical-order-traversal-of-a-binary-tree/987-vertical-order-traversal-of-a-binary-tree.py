# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [(root,0,0)]
        dic = OrderedDict()
        while queue:
            cur_num_node = len(queue)
            for i in range(cur_num_node):
                # if mark the root node as column 
                # then left node: column-1; right node: column+1
                node, depth, column = queue.pop(0)
                # print(node.val,depth,column)
                # print()
                try:
                    dic[column].append((depth, node.val))
                except:
                    dic[column] = [(depth, node.val)]
                if node.left: 
                    queue.append((node.left, depth+1, column-1))
                if node.right: 
                    queue.append((node.right, depth+1, column+1))
        result = []
        for i in sorted(dic.keys()):
            temp = []
            for j in sorted(dic[i]):
                temp.append(j[1])
            result.append(temp)
        return result