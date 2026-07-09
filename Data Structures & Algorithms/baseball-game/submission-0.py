class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        tot_sum = 0
        for op in operations:
            if op == '+':
                a = stk[-1] + stk[-2]
                tot_sum += a
                stk.append(a)
            elif op == 'D':
                a = stk[-1]*2
                tot_sum += a
                stk.append(a)
            elif op == 'C':
                a = stk.pop()
                tot_sum -= a
            else:
                stk.append(int(op))
                tot_sum += int(op)

        return tot_sum