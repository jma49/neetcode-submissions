class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brute force
        nums.sort()
        return nums[len(nums) - k]
        