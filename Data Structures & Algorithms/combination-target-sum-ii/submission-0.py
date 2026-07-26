class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, remain):
            if remain == 0:
                res.append(path[:])
                return
            if remain < 0:
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path, remain - nums[i])
                path.pop()

        nums.sort()
        res = []
        backtrack(0, [], target)
        return res
