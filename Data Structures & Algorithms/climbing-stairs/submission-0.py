from math import factorial as fact
class Solution:
    def climbStairs(self, n: int) -> int:
        if n % 2:
            num_2 = (n-1)//2
            num_1 = 1
        else:
            num_2 = n//2
            num_1 = 0
        
        ans = 0
        count = num_2 + num_1
        m = fact(count)
        f1, f2 = fact(num_1), fact(num_2)
        while num_2 >= 0:
            ans += m//(f1*f2)
            f1 *= ((num_1+1)*(num_1+2))
            if num_2>0:
                f2 = f2//num_2
            else:
                break
            num_2 -= 1
            num_1 += 2
            count += 1
            m *= count
        
        return ans
