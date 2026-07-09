class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        notes = [0, 0]
        for bill in bills:
            if bill == 5:
                notes[0] += 1
            elif bill == 10:
                if notes[0]:
                    notes[0] -= 1
                    notes[1] += 1
                else:
                    return False
            else:
                if notes[1] and notes[0]:
                    notes[1] -= 1
                    notes[0] -= 1
                elif notes[0] >= 3:
                    notes[0] -= 3
                else:
                    return False
        return True