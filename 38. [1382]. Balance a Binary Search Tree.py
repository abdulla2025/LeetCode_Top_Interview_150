# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        def build(vals):
            if not vals:
                return None
            mid = len(vals) // 2
            node = TreeNode(vals[mid])
            node.left = build(vals[:mid])
            node.right = build(vals[mid+1:])
            return node
        return build(inorder(root))
