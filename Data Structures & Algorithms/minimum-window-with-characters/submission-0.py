class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if n > m:
            return ''
        
        need = Counter(t)
        have = 0
        window = {}
        res = ""

        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                have += 1
            
            while have == len(need):
                if not res or right - left + 1 < len(res):
                    res = s[left: right + 1]

                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                left += 1
        return res

        


        


