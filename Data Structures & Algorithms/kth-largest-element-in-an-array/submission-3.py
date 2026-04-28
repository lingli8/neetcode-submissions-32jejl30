class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        output = []
        while len(output) < k:
            k_large = heapq.heappop(max_heap)
            output.append(k_large)
        k_th = len(output)-1
        return -output[k_th]