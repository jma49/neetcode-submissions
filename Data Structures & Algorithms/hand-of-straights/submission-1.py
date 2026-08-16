from _heapq import heapify
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
    
        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            start = min_heap[0]
            if count[start] == 0:
                heapq.heappop(min_heap)
                continue
            need = count[start]

            for card in range(start, start + groupSize):
                if count[card] < need:
                    return False
                count[card] -= need
        return True