class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        if num1 == "1":
            return num2
        if num2 == "1":
            return num1
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        vals = []
        m = len(num1)
        for digi in num2[::-1]:
            ans = 0
            carry = 0
            for i, bigi in enumerate(num1[::-1]):
                cd = int(digi) * int(bigi) + carry
                ans += (cd % 10)*(10**i)
                carry = cd // 10
                # print(cd, ans, carry)
            ans += carry*(10**m)
            # print(ans)
            vals.append(ans)
        ans = 0
        # print(vals)
        for i, val in enumerate(vals):
            ans += val*10**i


        return str(ans)