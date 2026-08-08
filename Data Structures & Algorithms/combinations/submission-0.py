class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def solve(curr_len, curr_ans, idx):
            if idx > n:
                if curr_len == k:
                    ans.append(curr_ans.copy())
                return
            
            curr_ans.append(idx)
            solve(curr_len+1, curr_ans, idx+1)
            curr_ans.pop()
            solve(curr_len, curr_ans, idx+1)
        
        ans = []
        solve(0, [], 1)
        return ans