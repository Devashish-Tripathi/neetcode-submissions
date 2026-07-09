import re
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        steps = 0
        wordSet = set(wordList)
        queue_begin, queue_end = deque([beginWord]), deque([endWord])
        m = len(beginWord)
        fromBegin, fromEnd = {beginWord:1}, {endWord:1}
        
        while queue_begin and queue_end:
            if len(queue_begin) > len(queue_end):
                queue_begin, queue_end = queue_end, queue_begin
                fromBegin, fromEnd = fromEnd, fromBegin
            
            for _ in range(len(queue_begin)):
                word = queue_begin.popleft()
                steps = fromBegin[word]
                for i in range(m):
                    for c in range(97, 123):
                        if chr(c) == word[i]:
                            continue
                        nei = word[:i] + chr(c) + word[i+1:]
                        if nei not in wordSet:
                            continue
                        if nei in fromEnd:
                            return steps + fromEnd[nei]
                        if nei not in fromBegin:
                            fromBegin[nei] = steps + 1
                            queue_begin.append(nei)
            
        return 0