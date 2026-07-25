class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        R_idx = deque([idx for idx in range(n) if senate[idx]=='R'])
        R_count = len(R_idx)
        D_idx = deque([idx for idx in range(n) if senate[idx]=='D'])
        D_count = len(D_idx)

        # print('before loop')
        # print('R:', R_idx, R_count)
        # print('D:', D_idx, D_count)
        # print('in loop')

        while R_idx and D_idx:
            for i in range(n):
                member = senate[i]
                if not R_count or not D_count:
                    break

                if member == 'R' and R_idx[0] == i:
                    D_idx.popleft()
                    D_count -= 1
                    if not D_count:
                        break
                    temp = R_idx.popleft()
                    R_idx.append(temp)
                
                elif member == 'D' and D_idx[0] == i:
                    R_idx.popleft()
                    R_count -= 1
                    if not R_count:
                        break 
                    temp = D_idx.popleft()
                    D_idx.append(temp)

                # print('after', i)
                # print('R:', R_idx, R_count)
                # print('D:', D_idx, D_count)

        if R_count:
            return "Radiant"
        else:
            return "Dire"                   
        