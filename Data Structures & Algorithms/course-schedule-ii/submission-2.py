class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #[0, 1]
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        # {0: [1], 1: [2], 2: [3], 3: []}
        cycle = set() # tracks if we hit the same node in one path twice
        visited = set() # tracks one complete path, doesn't revisit nodes
        output = []
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True    
            
        for crs in range(numCourses):
            if not dfs(crs): return []
        return output


    
        