class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pairs = {'}':'{', ')':'(', ']':'['}
        for ch in s:
            if ch in pairs.values():
                stk.append(ch)
            else:
                if len(stk) == 0:
                    return False
                elif stk[-1] == pairs[ch]:
                    stk.pop()
                else:
                    return False
        if len(stk) > 0:
            return False
        return True