class Solution:
    def minOperations(self, logs: List[str]) -> int:
        change = 0
        logs = deque(logs)
        while logs:
            op = logs.popleft()
            if op == './':
                continue
            elif op == '../':
                if change > 0:
                    change -= 1
            else:
                change += 1
        return change