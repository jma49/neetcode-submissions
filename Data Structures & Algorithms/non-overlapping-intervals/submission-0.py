class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return -1

        count = 1
        intervals.sort(key=lambda x:x[1])
        n = len(intervals)
        lastEnd = intervals[0][1]

        for i in range(1, n):
            if intervals[i][0] >= lastEnd:
                lastEnd = intervals[i][1]
                count += 1
        return n - count