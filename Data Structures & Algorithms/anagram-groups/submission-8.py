class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        fingerprint = []

        for word in strs:
            count = [0] * 26
            for letter in word:
                ans = ord(letter) - ord('a')
                count[ans]+=1
            fingerprint = tuple(count)        
            if fingerprint not in groups:
                groups[fingerprint] = []
                groups[fingerprint].append(word) 
            else:
                groups[fingerprint].append(word) 
        return list(groups.values())
'''
        for each word in the list count the letters and the frequency
        and based on those results the fingerprnt for each pattern would be detected
        based on that fingerprint in the dictionary it will be the key and the vlaues would be  the different words 
        to increment change the fingerrprnt we would use unicode
        ans = ord('a')-ord(letter) lers say the letter was b we know that b is 1 away from the letter a so the answer will give us 1 
        in the 
        i would want to go into the string or array of 0's and increment the 1st position because so far we have encountered b once 
        count[ans]+=1
'''