class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = base = window = max_window = 0
        for r in range(len(customers)):
            if grumpy[r]:
                window += customers[r]
            else:
                base += customers[r]
            
            if r-l+1 > minutes:
                if grumpy[l]:
                    window -= customers[l]
                l += 1
            max_window = max(max_window, window)

        return base + max_window