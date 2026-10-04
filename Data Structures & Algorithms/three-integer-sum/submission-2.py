class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return nums
        nums.sort()
        target = 0
        i = 0
        left = i + 1
        right = len(nums) - 1 
        result = []
        while i != len(nums):
            
            while left < right:
                if nums[i] + nums[left] + nums[right] > target:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < target:
                    left += 1    
                else: 
                #nums[i] + nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and  nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
                    left += 1
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            i += 1
            left = i + 1
            right = len(nums) - 1 
        return result
