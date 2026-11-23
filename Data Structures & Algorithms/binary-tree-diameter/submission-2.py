# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxd = 0

        def depth(curr):
            nonlocal maxd
            if not curr:
                return 0

            left = depth(curr.left)
            right = depth(curr.right)
            maxd = max(maxd, left + right)

            return 1 + max(left, right)
        
        depth(root)
        return maxd