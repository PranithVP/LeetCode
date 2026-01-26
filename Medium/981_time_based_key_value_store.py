class TimeMap:

    def __init__(self):
        self.map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""
        if len(self.map[key]) == 0:
            return ""

        left, right = 0, len(self.map[key]) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.map[key][mid][0] == timestamp:
                return self.map[key][mid][1]
            elif self.map[key][mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
            
        if right >= 0:
            return self.map[key][right][1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)