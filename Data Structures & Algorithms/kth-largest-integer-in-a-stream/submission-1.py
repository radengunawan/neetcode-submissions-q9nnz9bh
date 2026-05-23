import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        
        # Maintain only the k largest elements
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Add the new value to our heap
        heapq.heappush(self.min_heap, val)
        
        # If heap exceeds size k, pop the smallest
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # The root of the min-heap is the k-th largest element
        return self.min_heap[0]