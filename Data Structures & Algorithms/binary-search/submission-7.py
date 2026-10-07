class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
    
        low = 0
        high = len(nums)

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                # if mid is equal to target
                return mid

            if nums[mid] < target:
                low = mid + 1
            
            else: #nums[mid] > target:
                high = mid
            
        return -1