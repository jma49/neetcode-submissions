class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = "".join(filter(str.isalnum, s)).lower()
        n = len(strs)
        i, j = 0, n - 1
        while i < j:
            if strs[i] == strs[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

        