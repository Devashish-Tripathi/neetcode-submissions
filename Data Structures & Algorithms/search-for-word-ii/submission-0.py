class TrieNode():
    def __init__(self):
        self.children = {}
        self.idx = -1
        self.refs = 0

    def insert(self, word, idx):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            curr.refs += 1
        curr.idx = idx

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for idx, word in enumerate(words):
            root.insert(word, idx)
        m, n = len(board), len(board[0])
        ans = []
        rngm, rngn = range(m), range(n)
        def dfs(i, j, node):
            if i not in rngm or j not in rngn or board[i][j] == '*' or board[i][j] not in node.children:
                return 0
            temp = board[i][j]
            board[i][j] = '*'
            prev = node
            node = node.children[temp]
            found = 0
            if node.idx != -1:
                ans.append(words[node.idx])
                node.idx = -1
                found += 1
            
            found += dfs(i+1, j, node)
            found += dfs(i-1, j, node)
            found += dfs(i, j+1, node)
            found += dfs(i, j-1, node)

            board[i][j] = temp
            node.refs -= found
            if node.refs == 0:
                prev.children.pop(temp)
            return found
        

        for i in rngm:
            for j in rngn:
                root.refs -= dfs(i, j, root)
        
        return ans
            
        
        