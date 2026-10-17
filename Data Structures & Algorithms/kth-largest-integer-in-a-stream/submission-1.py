
import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heap = []

        self.k = k
        self.nums = nums
        self.heap = heap

        for x in range(len(self.nums)):
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, self.nums[x])
            else:
                if self.heap[0] < self.nums[x]:
                    heapq.heapreplace(self.heap, self.nums[x])

    def add(self, val: int) -> int:
        self.nums.append(val)

        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            if self.heap[0] < val:
                heapq.heapreplace(self.heap, val)

        return self.heap[0]
