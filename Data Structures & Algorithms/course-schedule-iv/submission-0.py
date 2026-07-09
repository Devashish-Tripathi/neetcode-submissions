class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        floyd = [[False] * numCourses for _ in range(numCourses)]
        ans = []

        for pre, crs in prerequisites:
            floyd[pre][crs] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    floyd[i][j] = floyd[i][j] or (floyd[i][k] and floyd[k][j])
        
        for u, v in queries:
            ans.append(floyd[u][v])
        
        return ans