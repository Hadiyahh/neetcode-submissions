class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        result = []
        
        i = 0
        while i < k:
            max_value = max(count.values())

            for key, value in count.items():
                if value == max_value:
                    ke = key
            result.append(ke)
            i+=1
            del count[ke]

        return result

