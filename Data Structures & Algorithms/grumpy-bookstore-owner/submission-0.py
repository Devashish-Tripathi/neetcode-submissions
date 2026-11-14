class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base = 0
        for idx, cust in enumerate(customers):
            if grumpy[idx] == 0:
                base += cust
        ans = base
        for start in range(0, len(customers)-minutes+1):
            m = 0
            for x in range(minutes):
                if grumpy[start+x] == 1:
                    m += customers[start+x]
            ans = max(ans, base+m)
        return ans