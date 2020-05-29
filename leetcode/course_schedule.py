class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        d = {i : set() for i in range(numCourses)}
        for p in prerequisites:
            d[p[0]].add(p[1])
        visited = [False] * numCourses
        def dfs(course, s):
            if course in s:
                return False
            s.add(course)
            visited[course] = True
            for x in d[course]:
                if not dfs(x, s):
                    return False
            s.remove(course)
            return True
        for i in range(numCourses):
            if not visited[i] and not dfs(i, set()):
                return False
        return True

s = Solution()
print(s.canFinish(3, [[0,1],[0,2],[1,2]]))
