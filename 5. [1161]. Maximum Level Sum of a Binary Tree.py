# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        
        if not root:
            return 0
        
        max_sum = float('-inf')
        max_level = 0
        current_level = 0
        
        queue = deque([root])
        
        while queue:
            current_level += 1
            level_size = len(queue)
            level_sum = 0
            
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
        
        return max_level