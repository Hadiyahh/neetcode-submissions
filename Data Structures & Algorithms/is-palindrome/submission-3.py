class Solution:
    def isPalindrome(self, s: str) -> bool:
    # Since s is made up of only printable ASCII characters I wont perform any checks for this
    # We will skip spaces tho
        # I could make another string with the join operator
        s = s.replace(" ","")
        s = "".join(c for c in s if c.isalpha() or c.isdigit())
        s = s.lower()
        print(s)
        i = 1 
        # Also different if its even or odd
        
        for char in s:
            if char != s[len(s) - i]:
                return False
            i += 1
        return True

