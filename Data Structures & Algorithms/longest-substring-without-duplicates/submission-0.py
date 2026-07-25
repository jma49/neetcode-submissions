class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set() # Determine whether a char already appeared
        left = 0
        longest = 0 

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            longest = max(right - left + 1, longest)
        return longest
