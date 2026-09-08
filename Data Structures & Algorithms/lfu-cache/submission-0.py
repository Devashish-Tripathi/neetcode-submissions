class LFUCache:

    def __init__(self, capacity: int):
        self.obj = {}
        self.usec = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.obj:
            self.usec[key] += 1
            return self.obj[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.obj:
            self.obj[key] = value
            self.usec[key] += 1
        else:
            if self.cap:
                self.cap -= 1
                self.obj[key] = value
                self.usec[key] = 1
            else:
                # this is where the fun begins
                # remove the least frequently used key
                lf = min(self.usec, key= self.usec.get)
                self.usec.pop(lf)
                self.obj.pop(lf)
                self.obj[key] = value
                self.usec[key] = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)