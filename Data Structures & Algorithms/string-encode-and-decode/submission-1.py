class Solution:

    def encode(self, strs: list[str])-> str:
        string = ""
        for word in strs: # loop over each word in the array
            string += str(len(word))
            string += "#"
            string += word
        return string

    def decode(self, s: str) -> list[str]:
        array = []
        i = 0
        while(i < len(s)):
            for j in range (i+1, len(s)):
                if s[j] == "#" and s[i].isdigit():
                    length = s[i:j]
                    start = j+1
                    end = int(length) + j + 1
                    array.append(s[start : end])
                    i = end
                    break
        return array

    