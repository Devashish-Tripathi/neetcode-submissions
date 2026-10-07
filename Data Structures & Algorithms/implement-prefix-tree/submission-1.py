class TrieNode:
    def __init__(self):
        self.data = {chr(x):None for x in range(ord('a'), ord('z')+1)}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.PTree = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.PTree
        for ch in word:
            if not curr.data[ch]:
                curr.data[ch] = TrieNode()
            curr = curr.data[ch]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.PTree
        for ch in word:
            if not curr.data[ch]:
                return False
            curr = curr.data[ch]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.PTree
        for ch in prefix:
            if not curr.data[ch]:
                return False
            curr = curr.data[ch]
        return True