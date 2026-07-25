class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        helper = set()
        for num in nums:
            if num in helper:
                return True
            else:
                helper.add(num)
        return False