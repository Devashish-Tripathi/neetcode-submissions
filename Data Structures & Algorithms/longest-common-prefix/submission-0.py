class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
    def lcp(self, prefixLen, word):
        node = self.root
        for i in range(min(len(word), prefixLen)):
            if word[i] not in node.children:
                return i
            node = node.children[word[i]]
        return min(len(word), prefixLen)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        miniIdx = 0
        for i in range(1, len(strs)):
            if len(strs[miniIdx]) > len(strs[i]):
                miniIdx = i
        
        trie = Trie()
        trie.insert(strs[miniIdx])
        prefixLen = len(strs[miniIdx])
        for i in range(len(strs)):
            prefixLen = trie.lcp(prefixLen, strs[i])
        
        return strs[0][:prefixLen]