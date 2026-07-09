class MinStack:

    def __init__(self):
        self.ls= []      
        self.minstk = []

    def push(self, val: int) -> None:
        self.ls.append(val)
        if not self.minstk or self.minstk[-1] >= val:
            self.minstk.append(val)

    def pop(self) -> None:
        x = self.ls.pop()
        if x == self.minstk[-1]:
            y = self.minstk.pop()
        return x

    def top(self) -> int:
        return self.ls[-1]

    def getMin(self) -> int:
        return self.minstk[-1]
