# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root)
        return self.result
    def dfs(self,node: TreeNode):
        if node is not None:
            self.dfs(node.left)
            self.result.append(node.val)
            self.dfs(node.right)