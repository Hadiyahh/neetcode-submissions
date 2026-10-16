# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return [] 
        queue = deque([root])
        stack = []
        
        while queue:
            
            level_size = len(queue)
            nums = []
            
            for _ in range(level_size):

                node = queue.popleft()
                nums.append(node.val)

                if node.left is not None:
                    queue.append(node.left)   

                if node.right is not None:
                    queue.append(node.right)    
                 
            stack.append(nums)

        return stack