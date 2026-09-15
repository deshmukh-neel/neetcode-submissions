class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()
        visiting = set()
        res = []

        def dfs(c):
            if c in visiting:
                return False
            if c in visited:
                return True
            visiting.add(c)
            for p in preMap[c]:
                if not dfs(p): return False
            visiting.remove(c)
            visited.add(c)
            res.append(c)
            return True

        for c in range(numCourses):
            if not dfs(c): return []
        return res