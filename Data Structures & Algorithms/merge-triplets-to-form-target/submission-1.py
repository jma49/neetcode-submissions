class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if not triplets:
            return False

        
        valid = [t for t in triplets if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]]

        if not valid:
            return False

        ai = max(t[0] for t in valid)
        bi = max(t[1] for t in valid)
        ci = max(t[2] for t in valid)

        return [ai, bi, ci] == target