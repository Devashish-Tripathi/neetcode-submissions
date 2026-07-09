class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        numMap = {
            '2': (['a', 'b', 'c'], 3),
            '3': (['d', 'e', 'f'], 3),
            '4': (['g', 'h', 'i'], 3),
            '5': (['j', 'k', 'l'], 3),
            '6': (['m', 'n', 'o'], 3),
            '7': (['p', 'q', 'r', 's'], 4),
            '8': (['t', 'u', 'v'], 3),
            '9': (['w', 'x', 'y', 'z'], 4)
        }

        ans = [""]
        for digi in digits:
            temp = []
            posChars = numMap[digi][0]
            for currStr in ans:
                for ch in posChars:
                    temp.append(currStr+ch)
            ans = temp        
        return ans