class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i, n = 0, len(intervals)

        # 
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        
        # 
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        ans.append(newInterval)
        
        # 
        for j in range(i, n):
            ans.append(intervals[j])
        return ans
