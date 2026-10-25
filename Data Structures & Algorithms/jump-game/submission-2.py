class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        jump_position = nums[0]
        
        for i, num in enumerate(nums):
            if i <= jump_position:
                jump_position = max(jump_position, num+i)
            
        if jump_position >= len(nums)-1:
            return True
        else:
            return False