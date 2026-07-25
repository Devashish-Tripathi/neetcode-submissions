class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        if m < n:
            str1, str2 = str2, str1
            m, n = n, m
        
        # str1 would remain bigger
        for i in range(n):
            x = str2[:n-i]
            x_len = n-i
            if m % x_len == 0 and n % x_len == 0:
                # divisible
                if x*(m//x_len) == str1 and x*(n//x_len) == str2:
                    return x
        
        return ""
               