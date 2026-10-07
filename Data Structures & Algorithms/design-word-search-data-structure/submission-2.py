class TrieNode:
    def __init__(self):
        self.data = {chr(x):None for x in range(ord('a'), ord('z')+1)}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if not curr.data[ch]:
                curr.data[ch] = TrieNode()
            curr = curr.data[ch]
        curr.isEnd = True 

    def search(self, word: str) -> bool:
        def dfs(idx, curr):
            if idx == len(word):
                return curr.isEnd

            if word[idx] == '.':
                for ch in curr.data.keys():
                    if curr.data[ch] and dfs(idx+1, curr.data[ch]):
                        return True
                return False
            else:
                if curr.data[word[idx]] and dfs(idx+1, curr.data[word[idx]]):
                    return True
                return False
        return dfs(0, self.root)
                

