class Solution:
    def largestGoodInteger(self, num: str) -> str:
        curr = -1
        i = 0
        while i < len(num)-2:
            if num[i] == num[i+1] == num[i+2]:
                curr = max(curr, int(num[i]))
                i += 3
            elif num[i] == num[i+1]:
                i += 2
            else:
                i += 1 
                
        return str(curr)*3 if curr != -1 else ""