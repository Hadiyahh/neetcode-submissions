class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]: 
            # rotation has occurred and my left side is sorted
                if nums[left] <= target < nums[mid]: # the target is in the left sorted
                    right = mid - 1 # we dont need to search through the left side anymore
                else:
                    left = mid + 1
            else:# nums[left] > nums[mid] and nums[mid] < nums[right]:
            # rotation has occurred and my ride side is sorted
                if nums[mid] < target <= nums[right]: # the target is in the right sorted
                    left = mid + 1
                else:
                    right = mid - 1

        return -1