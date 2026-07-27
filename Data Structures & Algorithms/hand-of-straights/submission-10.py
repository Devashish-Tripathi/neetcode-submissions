from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            # not divisible meaning cannot divide using the given group size
            return False
        
        if groupSize == 1:
            return True

        cnt_hand = sorted(Counter(hand).most_common())
        # print(cnt_hand)
        n_groups = n//groupSize
        # print(n_groups)
        ans = [[-1] for _ in range(n_groups)]
        grpSizes = [0 for _ in range(n_groups)]
        for value, counts in cnt_hand:
            iter_ans = 0
            # if counts > n_groups:
                # return False
            while counts:
                # print(ans)
                # print(grpSizes)
                # print('iter_ans before if:', iter_ans)
                if iter_ans >= n_groups:
                    iter_ans = 0
                # print('iter_ans after if:', iter_ans)
                while grpSizes[iter_ans] == groupSize:
                    iter_ans += 1
                    # print(iter_ans, grpSizes[iter_ans])
                
                if ans[iter_ans][-1] == -1:
                    ans[iter_ans][-1] = value
                    grpSizes[iter_ans] += 1
                    counts -= 1
                elif ans[iter_ans][-1]+1 == value:
                    ans[iter_ans].append(value)
                    grpSizes[iter_ans] += 1
                    counts -= 1
                else:
                    return False
                
                iter_ans += 1
        
        return True
                