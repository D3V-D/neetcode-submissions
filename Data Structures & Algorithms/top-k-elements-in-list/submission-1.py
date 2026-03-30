import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        # Map vals to freq
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        
        # Use min-heap to get k-largest freqs
        min_heap = []
        for num in frequencies:
            if len(min_heap) < k:
                # heappush evaluates off first element of tuple
                heapq.heappush(min_heap, (frequencies[num], num))
            else:
                heapq.heappushpop(min_heap, (frequencies[num], num))

        # array from second values
        return [val[1] for val in min_heap]
