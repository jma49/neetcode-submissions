from heapq import heappop, heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # {u: (v, w)}
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        distances = {k :0}
        heap = [(0, k)]

        while heap:
            dist, node = heappop(heap)
            for neighbor, weight in graph[node]:
                if dist + weight < distances.get(neighbor, float('inf')):
                    distances[neighbor] = dist + weight
                    heappush(heap, (dist + weight, neighbor))
        
        if len(distances) != n:
            return -1
        return max(distances.values())