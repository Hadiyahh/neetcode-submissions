class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_before = []
        running = 1
        for num in nums:
            product_before.append(running)
            running = running * num
        running = 1
        i = len(nums) - 1
        for num in reversed(nums):
            product_before[i] = product_before[i] * running
            running = running * num
            i -= 1
        return product_before