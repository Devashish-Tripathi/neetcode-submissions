class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        if n <= 1:
            return n
        # process cars closer to the target
        combined = [(position[i], speed[i]) for i in range(n)]
        combined = sorted(combined, reverse= True)
        stk = [(target-combined[0][0])/combined[0][1]]
        for pos, spd in combined[1:]:
            time = (target-pos)/spd
            if time > stk[-1]:
                stk.append(time)

        return len(stk)
        