class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left) // 2
       
            # Python allows negative indexing
            if nums[mid-1] > nums[mid]: # if a value thats before me is greater than me 
                return nums[mid]
            elif mid is not right and nums[mid+1] < nums[mid]: # if a value after me is less than me 
                return nums[mid+1] 
            elif nums[mid] >= nums[right]:
                left = mid + 1
            else:# nums[mid] < nums[left]:
                right = mid - 1
               
        return nums[mid]