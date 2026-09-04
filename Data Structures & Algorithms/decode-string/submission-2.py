class Solution:
    def decodeString(self, s: str) -> str:
        nums = []
        ans = ""        
        bracket_open = []
        idx = 0
        n = len(s)
        while idx < n and not s[idx].isdigit():
            ans += s[idx]
            idx += 1
        
        while idx < n:
            curr_num = ''
            while s[idx].isdigit():
                curr_num += s[idx]    
                idx += 1
            if curr_num:
                nums.append(int(curr_num))
            else:
                ch = s[idx]
                if ch == '[':
                    bracket_open.append('')
                elif ch.isalpha():
                    if not bracket_open:
                        ans += ch
                    else:
                        bracket_open[-1] += ch
                else:
                    curr = bracket_open.pop()
                    overall = curr * nums.pop() 
                    if not bracket_open:
                        ans += overall
                    else:
                        bracket_open[-1] += overall
                idx += 1
        
        return ans
