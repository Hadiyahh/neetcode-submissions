class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = "".join(c for c in s if c.isalpha() or c.isdigit())
        s = s.lower()
        i = 1 
        
        for char in s:
            if char != s[len(s) - i]:
                return False
            i += 1
        return True

