class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            dis = x*x + y*y
            heapq.heappush(max_heap, [-dis,x,y])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        res = []
        for dis,x,y in max_heap:
            res.append([x,y])
        return res