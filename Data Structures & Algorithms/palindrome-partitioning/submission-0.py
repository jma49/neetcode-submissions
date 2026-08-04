class Solution:
    def partition(self, s: str) -> List[List[str]]:

        ans = []

        def isPalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left = left + 1
                right = right - 1
            return True

        def backtrack(start, path):
            if start == len(s):
                ans.append(path[:])
                return
            
            for char in range(start, len(s)):
                if isPalindrome(s, start, char):
                    path.append(s[start:char + 1])
                    backtrack(char + 1, path)
                    path.pop()
        
        backtrack(0, [])
        return ans

