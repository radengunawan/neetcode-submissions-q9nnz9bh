class TimeMap:

    def __init__(self):
        self.simpen = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.simpen:
            self.simpen[key] = []
        self.simpen[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        hazil = ""
        daftar_value = self.simpen.get(key, [])

        L, R = 0, len(daftar_value) - 1

        while (L <= R):
            M = L + (R - L)//2

            if daftar_value[M][1] <= timestamp:
                hazil = daftar_value[M][0]
                L = M + 1
            #elif daftar_value[M][1] > timestamp
            else:
                R = M - 1


        return hazil
