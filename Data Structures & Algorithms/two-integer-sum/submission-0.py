

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}

        for i in range(n):
            subtract = target - nums[i]
            if subtract in seen:
                return [seen[subtract], i]
            else:
                seen[nums[i]] = i
        return []
