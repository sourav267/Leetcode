class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.heap = []
        self.k = k
        
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        
        heapq.heappush(self.heap, val)
        
        # if after adding the new item causes 
        # the heap size to increase beyond k, 
        # then pop out the smallest element 
        if len(self.heap) > self.k: 
            heapq.heappop(self.heap)
            
        return self.heap[0] # the root element
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)