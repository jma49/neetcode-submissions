class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        count1 = Counter(s1)
        window = Counter(s2[:n])
        if window == count1:
            return True

        for i in range(n, m):
            window[s2[i]] += 1
            left = s2[i - n]
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            if window == count1:
                return True
        
        return False
