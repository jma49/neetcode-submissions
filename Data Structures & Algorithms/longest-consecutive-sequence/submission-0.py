class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        
        # {2， 20， 4， 10 ，3， 5}
        for i in range(len(nums)):
            if nums[i] - 1 not in numSet:
                curr = nums[i]
                length = 1
                while curr + 1 in numSet:
                    curr += 1
                    length += 1
                longest = max(length, longest) 
        return longest

                