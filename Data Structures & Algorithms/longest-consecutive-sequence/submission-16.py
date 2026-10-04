class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # nums.sort() # .sort() method is \(O(n \log n)\) 
        seen = set()
        m = 0
        count = 0
        for i in nums:
            seen.add(i)
        x = 0
      
        for num in nums:
            if num-1 not in seen:
                count = 0 
                x = 0
                while num + x in seen:
                    count += 1
                    x+=1
                if m < count:
                    m = count
                
        return m
