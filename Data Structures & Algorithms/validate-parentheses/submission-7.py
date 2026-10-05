class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        stack = []
        for char in s:
            if char in '})]':
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if stack: 
            return False
        else:
            return True