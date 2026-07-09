class Solution:
    def checkValidString(self, s: str) -> bool:
        stk_left, stk_star = [], []
        for i, ch in enumerate(s):
            if ch == '(':
                stk_left.append(i)
            elif ch == '*':
                stk_star.append(i)
            else:
                if stk_left:
                    stk_left.pop()
                elif stk_star:
                    stk_star.pop()
                else:
                    return False
        
        while stk_left and stk_star and stk_left[-1] < stk_star[-1]:
            stk_left.pop()
            stk_star.pop()
        
        if stk_left:
            return False
        
        return True