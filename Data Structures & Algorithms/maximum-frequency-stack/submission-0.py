class FreqStack:

    def __init__(self):
        self.max_count = 0
        self.count_table = {}
        self.stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        self.count_table[val] = self.count_table.get(val, 0) + 1
        self.max_count = max(self.max_count, self.count_table[val])

    def pop(self) -> int:
        temp = []
        while self.count_table[self.stk[-1]] < self.max_count:
            temp.append(self.stk.pop())
        to_ret = self.stk.pop()
        
        # print('after getting the max element:')
        # print(self.stk)
        # print(temp)

        self.count_table[to_ret] -= 1
        flag = False
        while self.stk:
            if self.count_table[self.stk[-1]] == self.max_count:
                flag = True
                break
            temp.append(self.stk.pop())
        
        if not flag:
            self.max_count -= 1

        # print('after searching for next big shot')
        # print(temp)
        # print(self.stk)
        
        while temp:
            self.stk.append(temp.pop())
        
        # print('Final stack')
        # print(self.stk)
        
        return to_ret


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()