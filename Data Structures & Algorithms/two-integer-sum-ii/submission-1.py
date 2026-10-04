class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # S ince the solution must take O(1) additional space that means we cant use a dict and do the method we know which is target - the current index we are on
        # so we know we will be using pointers  
        # another option would be to do 2 for loops but that will bee O(n^2)
        # what if i put the numberrs ive seen in a set? extra  space?


        # Its in increasing order so the next biggest will be right after it

        left = 0
        right = len(numbers) - 1
        if len(numbers) == 0 or len(numbers) == 1:
            return numbers
        while left < right:
            if numbers[right] + numbers[left] > target: 
                right -= 1
            if numbers[right] + numbers[left] < target: 
                left += 1
            if numbers[right] + numbers[left] == target:
                return [left + 1, right + 1]
        
        return numbers