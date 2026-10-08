# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
     
        elif p is not None and q is not None:
            if p.val != q.val:
                return False

            a = self.isSameTree(p.right, q.right)
            b = self.isSameTree(p.left, q.left)
        else:
            return False
        return a and b