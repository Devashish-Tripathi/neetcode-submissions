class Solution:
    def makeGood(self, s: str) -> str:
        ans = []
        for ch in s:
            if ans and max(ord(ans[-1]), ord(ch))-97 == min(ord(ans[-1]), ord(ch))-65:
                    ans.pop()
            else:
                ans.append(ch)
        return ''.join(ans)