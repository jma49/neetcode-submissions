class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = Counter(s)
        count_t = Counter(t)

        for char in count_s:
            if count_s[char] != count_t.get(char):
                return False
        return True