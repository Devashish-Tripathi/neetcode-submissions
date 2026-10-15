class Solution:
    def minOperations(self, logs: List[str]) -> int:
        change = 0
        for op in logs:
            if op == './':
                continue
            elif op == '../':
                if change > 0:
                    change -= 1
            else:
                change += 1
        return change