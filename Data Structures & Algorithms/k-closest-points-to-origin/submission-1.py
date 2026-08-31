import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            x, y = points[i]
            distance = x * x + y * y
        
            if len(heap) < k:
                heapq.heappush(heap, (-distance, i))
            elif heap[0][0] < -distance:
                heapq.heappushpop(heap, (-distance, i))
        return [points[p[1]] for p in heap]