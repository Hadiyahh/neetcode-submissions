class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = "".join(c for c in s if c.isalpha() or c.isdigit())
        s = s.lower()
        i = 1 
        j = 0
        while j < len(s)/2:
            if s[j] == s[len(s) - j - 1]:
                j += 1
            else:
                return False    
        # for char in s:
        #     if char != s[len(s) - i]:
        #         return False
        #     i += 1
        return True

