class FreqStack:

    def __init__(self):
        self.count_table = {}
        self.stacks = [[]]
        self.n_stacks = 1

    def push(self, val: int) -> None:
        self.count_table[val] = self.count_table.get(val, 0) + 1
        if self.count_table[val] == self.n_stacks:
            self.stacks.append([])
            self.n_stacks += 1

        self.stacks[self.count_table[val]].append(val)

    def pop(self) -> int:
        to_ret = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
            self.n_stacks -= 1
        self.count_table[to_ret] -= 1
        return to_ret