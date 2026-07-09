class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = {x:set() for x in range(1, n+1)}
        for tr in trust:
            people[tr[0]].add(tr[1])
        candidate = 0
        print(people)
        for k, v in people.items():
            if not v:
                if candidate == 0:
                    candidate = k
                else:
                    return -1
        if not candidate:
            return -1
        
        for v in people.values():
            if v and candidate not in v:
                return -1
        
        return candidate