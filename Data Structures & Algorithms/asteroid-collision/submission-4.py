class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for ast in asteroids:
            while stk and stk[-1] > 0 and ast < 0:
                if stk[-1] + ast < 0:
                    stk.pop()
                elif stk[-1] + ast == 0:
                    stk.pop()
                    ast = 0
                else:
                    ast = 0
            if ast:
                stk.append(ast)
            

        return stk
