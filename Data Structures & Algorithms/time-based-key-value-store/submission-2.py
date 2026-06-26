class TimeMap:

    def __init__(self):
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        L, R = 0, len(values) - 1
        while L <= R:
            M = (L + R) // 2
            if values[M][1] <= timestamp:
                res = values[M][0]
                L = M + 1
            else:
                R = M - 1
        return res