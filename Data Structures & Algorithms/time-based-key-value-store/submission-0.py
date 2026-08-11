class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        records = self.store[key]
        if not records:
            return ""
        
        n = len(records)
        left, right = 0, n - 1
        result = ""
        
        while left <= right:
            mid = left + (right - left) // 2
            if records[mid][0] <= timestamp:
                result = records[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return result

