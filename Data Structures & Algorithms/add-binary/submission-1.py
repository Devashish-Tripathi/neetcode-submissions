class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        na, nb = len(a), len(b)
        if na < nb:
            a, b = b, a
            na, nb = nb, na
        # a is larger
        su, car = 0, 0
        i, j = na-1, nb-1
        while j > -1:
            if a[i] == '0' and b[j] == '0':
                su = car
                car = 0
            elif (a[i] == '1' and b[j] == '0') or (a[i] == '0' and b[j] == '1'):
                su = (1+car)%2
                car = (1+car)//2
            else:
                su = car
                car = 1
            ans += "1" if su else "0"
            i -= 1
            j -= 1
        
        while i > -1:
            su = (int(a[i])+car)%2
            car = (int(a[i])+car)//2
            ans += "1" if su else "0"
            i -= 1
        
        if car:
            ans += '1'
            
        return ans[::-1]