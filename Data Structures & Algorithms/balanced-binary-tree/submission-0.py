# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        diff = 0

        def depth(curr):
            nonlocal diff

            if not curr:
                return 0
            
            left = depth(curr.left)
            right = depth(curr.right)
            diff = max(diff, abs(right - left))
            return 1 + max(left, right)
        
        depth(root)
        return abs(diff) <= 1