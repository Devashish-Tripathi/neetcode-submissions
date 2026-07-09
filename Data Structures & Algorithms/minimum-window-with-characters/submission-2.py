from copy import deepcopy
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)

        cntDct = {chr(x):0 for x in range(ord('A'), ord('z')+1) if chr(x) in t}
        for ch in t:
            cntDct[ch] += 1

        start, end = 0, 0
        best_start, best_end = 0, float('inf')
        
        # We use a single loop to expand the right bound
        while end < n:
            # Check the current window s[start:end+1]
            cntDct_copy = deepcopy(cntDct)
            currStr = s[start:end+1]
            
            # Your exact validation loop
            for ch in currStr:
                if ch in cntDct_copy:
                    cntDct_copy[ch] -= 1
            
            numpos = sum([1 for x in cntDct_copy.values() if x > 0]) 
            
            # If valid, we try to shrink from the left (start)
            if numpos == 0:
                while start <= end:
                    # Update our best window if this one is smaller
                    if (end + 1 - start) < (best_end - best_start):
                        best_start = start
                        best_end = end + 1
                    
                    # Try shrinking from the left
                    start += 1
                    
                    # Re-verify if it's still valid after shrinking
                    cntDct_copy2 = deepcopy(cntDct)
                    for ch in s[start:end+1]:
                        if ch in cntDct_copy2:
                            cntDct_copy2[ch] -= 1
                    
                    # If it's no longer valid, stop shrinking and go back to expanding
                    if sum([1 for x in cntDct_copy2.values() if x > 0]) > 0:
                        break
            
            end += 1

        return "" if best_end == float('inf') else s[best_start:best_end]



        # start, end = 0, n
        # best_start, best_end = start, end
        # while start <= end:
        #     cntDct_copy = deepcopy(cntDct)
        #     found = False
        #     currStr = s[start:end]
        #     for ch in currStr:
        #         if ch in cntDct_copy:
        #             cntDct_copy[ch] -= 1
            
        #     numpos = sum([1 for x in cntDct_copy.values() if x > 0]) 
        #     if numpos != 0:
        #         found = False
        #         if end-start == n:
        #             return ""
        #     else:
        #         found = True
        #         best_start = start
        #         best_end = end
        #     print(s[start], s[end-1])
        #     print(s[start] in cntDct)
        #     print(s[end-1] in cntDct)
        #     if s[start] not in cntDct:
        #         start += 1
        #     elif s[end-1] not in cntDct:
        #         end -= 1
        #     else:
        #         print(cntDct_copy)
        #         if cntDct_copy[s[start]] < 0 and cntDct_copy[s[end-1]] == 0:
        #             start += 1
        #         elif cntDct_copy[s[end-1]] < 0 and cntDct_copy[s[start]] == 0:
        #             end -= 1
        #         elif cntDct_copy[s[end-1]] < 0 and cntDct_copy[s[start]] < 0:
        #             if cntDct_copy[s[end-1]] < cntDct_copy[s[start]]:
        #                 end -= 1
        #             else:
        #                 start += 1
        #         else:
        #             if s[start] == s[end-1]:
        #                 start += 1
        #                 end = n
        #             else:
        #                 break

        #     del cntDct_copy 

        return s[best_start:best_end]