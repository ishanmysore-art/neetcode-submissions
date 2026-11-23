# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [], []
        curr = root
        prev = None

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            peek = stack[-1]

            if peek.right and prev != peek.right:
                curr = peek.right
            else:
                res.append(peek.val)
                prev = stack.pop()
        
        return res