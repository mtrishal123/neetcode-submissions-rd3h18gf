class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visitSet = set()
        mapper = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            mapper[crs].append(pre)
        def dfs(crs):
            if crs in visitSet:
                return False
            if mapper[crs] == []:
                return True
            visitSet.add(crs)
            for pre in mapper[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            mapper[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True