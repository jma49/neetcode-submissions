class Solution:
    def jump(self, nums: List[int]) -> int:
        farest = 0
        curr_end = 0
        jumps = 0
        for i in range(len(nums) - 1):
            farest = max(farest, i + nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = farest
        return jumps