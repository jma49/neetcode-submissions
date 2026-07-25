class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in seen:
                return [seen[sub], i]
            else:
                seen[nums[i]] = i
        return []