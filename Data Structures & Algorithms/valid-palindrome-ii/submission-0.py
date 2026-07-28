class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n-1
        invalid_idxs = set()

        def check_pali(avoid):
            l, r = 0, n-1
            while l <= r:
                if avoid == -1:
                    if s[l] == s[r]:
                        l += 1
                        r -= 1
                    else:
                        return False, l, r
                else:
                    # print(l, r, s[l], s[r], s[avoid])
                    if s[l] == s[r] and s[l] != s[avoid]:
                        l += 1
                        r -= 1
                    elif s[l] == s[avoid]:
                        l += 1
                    elif s[r] == s[avoid]:
                        r -= 1
                    else:
                        return False, l, r
            return True, l, r
        
        is_pali, l_idx, r_idx = check_pali(-1)
        if is_pali:
            return True
        else:
            is_pali, _, _ = check_pali(l_idx)
            if is_pali:
                return True
            is_pali, _, _ = check_pali(r_idx)
            return is_pali
