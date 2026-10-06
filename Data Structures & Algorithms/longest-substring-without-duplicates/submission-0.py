class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        best = 0
        seen = set()
       
        for right in range(len(s)): 
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            current_best = right - left + 1
            best = max(best, current_best)

        return best
            

