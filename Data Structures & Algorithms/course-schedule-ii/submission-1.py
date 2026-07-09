class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs_of = {x:set() for x in range(numCourses)}
        for to_take, needed in prerequisites:
            prereqs_of[to_take].add(needed)
        prereqs_of = {k:v for k, v in sorted(prereqs_of.items(), key= lambda x: len(x[1]))}
        indegree_of = {k: len(v) for k, v in prereqs_of.items()}
        ans = []
        queue = deque()
        visited = set()
        for k, v in indegree_of.items():
            if v > 0: break
            queue.append(k)
        while queue:
            # for i in range(len(queue)):
                course = queue.popleft()
                visited.add(course)
                for k, v in prereqs_of.items():
                    if course in v:
                        indegree_of[k] -= 1
                        if indegree_of[k] == 0:
                            queue.append(k)
                ans.append(course)
        if len(ans) != numCourses:
            return []
        return ans

