class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
                '}':'{',
                ')':'(',
                ']':'['
            }
        stack = []
        for char in s:
            if stack and char in "])}":
                # print("char",char)
                # print("stack", stack)
                # print("pairs[char]", pairs[char])
                if stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if len(stack) == 0:
            return True
        else:
            return False