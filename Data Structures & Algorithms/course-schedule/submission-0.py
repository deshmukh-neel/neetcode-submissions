class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create the adjacency map
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # need a set to track visited nodes

        visited = set()

        # DFS
        def dfs(crs):
            # base cases
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True

            visited.add(crs)
            for p in preMap[crs]:
                if not dfs(p): return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
        
