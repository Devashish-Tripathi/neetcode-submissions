class StockSpanner:

    def __init__(self):
        self.stk = []  #(price, span)

    def next(self, price: int) -> int:
        span_length = 1
        stk2 = []
        while self.stk and self.stk[-1][0] <= price:
            span_length += self.stk[-1][1]
            self.stk.pop()
        
        self.stk.append((price, span_length))

        return span_length



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)