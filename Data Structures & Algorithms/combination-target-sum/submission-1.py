class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(start, path, remain):
            if remain == 0:
                res.append(path[:])
                return
            if remain < 0:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                # because we can reuse the num, so this should i not i + 1
                backtrack(i, path, remain - nums[i])
                path.pop()

        backtrack(0, [], target)
        return res