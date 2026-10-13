class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        results = [0]
        while left < right:
            #heights[left] + heights[right]
            results.append(max(results[-1],(min(heights[left],heights[right]) * (right - left))))
            if heights[left] < heights[right]:
                left += 1
            else:# if heights[left] > heights[right]:
                right -= 1
        #print(results)
        return max(results)