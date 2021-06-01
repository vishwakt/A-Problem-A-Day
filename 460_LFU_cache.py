from collections import OrderedDict, defaultdict


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.minFreq = 1
        self.keyToValFreq = {}
        self.freqToKeyValue = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.keyToValFreq:
            print(-1)
            return -1
        val, freq = self.keyToValFreq.pop(key)
        self.freqToKeyValue[freq].pop(key)
        if len(self.freqToKeyValue[freq]) == 0 and freq == self.minFreq:
            self.minFreq += 1
        self.freqToKeyValue[freq+1][key] = None
        self.keyToValFreq[key] = (val, freq + 1)
        print(val)
        return val

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return

        if key in self.keyToValFreq:
            self.get(key)
            self.keyToValFreq[key] = (value, self.keyToValFreq[key][1])
            return

        if self.cap <= len(self.keyToValFreq):
            delKey, _ = self.freqToKeyValue[self.minFreq].popitem(last=False)
            self.keyToValFreq.pop(delKey)

        self.keyToValFreq[key] = (value, 1)
        self.freqToKeyValue[1][key] = None
        self.minFreq = 1


if __name__ == "__main__":
    obj = LFUCache(5)
    param_1 = obj.get(1)
    obj.put(1,1)
    param_2 = obj.get(1)
