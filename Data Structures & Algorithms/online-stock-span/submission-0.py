class StockSpanner:

    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        span_length = 1
        stk2 = []
        while self.stk and self.stk[-1] <= price:
            stk2.append(self.stk.pop())
            span_length += 1
        
        while stk2:
            self.stk.append(stk2.pop())
        
        self.stk.append(price)

        return span_length



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)