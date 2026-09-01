class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k (1, max(piles))

        left, right = 1, max(piles)
        while left < right:
            mid = (right + left) // 2
            if sum((pile - 1) // mid + 1 for pile in piles) <= h:
                right = mid
            else:
                left = mid + 1
        return left
