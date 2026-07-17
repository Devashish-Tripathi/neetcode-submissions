class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        lenWord = len(word)
        x, y = len(board), len(board[0])
        rng_x, rng_y = range(x), range(y)
        
        def dfs(k, i, j, chain):
            # print(k, i, j)

            if board[i][j] == word[k]:
                k += 1
                # print('here', k, i, j)
            else:
                return False
            if k == lenWord:
                # if curr_word == word:
                # print(i, j, 'done')
                return True
                # return False
            
            # get neighbours
            nbrs = []    
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if (ni, nj) not in chain and ni in rng_x and nj in rng_y:
                    nbrs.append((ni, nj))
            

            for ni, nj in nbrs:
                chainc = chain.copy()
                chainc.append((ni, nj))
                if dfs(k, ni, nj, chainc):
                    return True
            
            return False
        
        for m in rng_x:
            for n in rng_y:
                if dfs(0, m, n, [(m, n)]):
                    return True
        
        return False

