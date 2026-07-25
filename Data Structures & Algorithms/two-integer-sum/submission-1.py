class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}

        # seen {3:0, 4:1, 5:2, 6:3}
        for i in range(n):
            sub = target - nums[i]
            if sub in seen:
                return [seen[sub], i]
            else:
                seen[nums[i]] = i
        return []