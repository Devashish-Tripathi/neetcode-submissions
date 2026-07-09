import re
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        steps = 0
        wordList = set(wordList)
        queue = deque([beginWord])
        visited = set()
        m = len(beginWord)
        while queue:
            for x in range(len(queue)):
                word = queue.popleft()
                visited.add(word)
                if word == endWord:
                    return steps+1
                nbr_patterns = [word[:i] + '.' + word[i+1:] for i in range(m)]
                for pattern in nbr_patterns:
                    queue.extend([matched for matched in wordList if (re.match(pattern, matched) and matched in wordList and matched not in visited)])
            steps += 1
            
        return 0