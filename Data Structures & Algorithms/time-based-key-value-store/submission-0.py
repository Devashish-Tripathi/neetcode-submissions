class TimeMap:

    def __init__(self):
        self.tstamp_kv, self.tstamp_kt = dict(), dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.tstamp_kt.get(key, None):
            self.tstamp_kv[key] = [value]
            self.tstamp_kt[key] = [timestamp]
        else:
            self.tstamp_kv[key].append(value)
            self.tstamp_kt[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        tstamps = self.tstamp_kt.get(key, None)
        if not tstamps: return ""
        if timestamp < tstamps[0]:
            return ""
        lo, hi = 0, len(tstamps)-1
        possibles = []
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if tstamps[mid] <= timestamp:
                possibles.append(mid)
                lo = mid+1
            else:
                hi = mid-1
        if not possibles: return ""
        return self.tstamp_kv[key][max(possibles)]

