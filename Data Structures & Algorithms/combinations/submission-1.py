class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def solve(curr_ans, idx):
            if len(curr_ans) == k:
                ans.append(curr_ans.copy())
                return
            
            for i in range(idx, n+1):
                curr_ans.append(i)
                solve(curr_ans, i+1)
                curr_ans.pop()
        
        ans = []
        solve([], 1)
        return ans