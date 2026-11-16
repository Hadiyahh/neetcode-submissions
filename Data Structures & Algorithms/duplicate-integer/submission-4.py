class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        a = False
        for num in nums:
            if num in seen:
                a = True
                break
            else: 
                a = False
                seen.add(num)
        return a