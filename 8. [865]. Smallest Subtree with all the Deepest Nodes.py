# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return (0, None)
            
            left_depth, left_subtree = dfs(node.left)
            right_depth, right_subtree = dfs(node.right)
            current_depth = 1 + max(left_depth, right_depth)
            
            if left_depth == right_depth:
                return (current_depth, node)
            elif left_depth > right_depth:
                return (current_depth, left_subtree)
            else:
                return (current_depth, right_subtree)
        _, result = dfs(root)
        return result