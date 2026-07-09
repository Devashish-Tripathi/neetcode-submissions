class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                ch = word[i]
                if ch == '.':
                    for child in curr.children:
                        if child and dfs(i+1, child):
                            return True
                    return False
                else:
                    idx = ord(ch) - ord('a')
                    if not curr.children[idx]:
                        return False
                    curr = curr.children[idx]
            return curr.isEnd
        
        return dfs(0, self.root)

        
