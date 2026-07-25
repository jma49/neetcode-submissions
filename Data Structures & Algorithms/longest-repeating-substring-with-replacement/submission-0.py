class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        count = {}
        left = 0
        result = 0
        n = len(s)

        for right in range(n):
        # (right - left + 1) - max_freq <= k
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result