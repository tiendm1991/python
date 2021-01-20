# https://leetcode.com/problems/redundant-connection-ii/discuss/108070/Python-O(N)-concise-solution-with-detailed-explanation-passed-updated-testcases
class Solution:
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        uf = [i for i in range(n + 1)]

        def find(v):
            if v != uf[v]:
                uf[v] = find(uf[v])
            return uf[v]

        def union(u, v):
            ru = find(u)
            rv = find(v)
            if ru == rv:
                return False
            uf[rv] = ru
            return True

        def isCycle(candidate):
            u, v = candidate[0], candidate[1]
            while u in parent:
                if parent[u] == v:
                    return True
                u = parent[u]
            return False

        parent = {}
        # candidate is vertex has 2 parent
        candidates = []
        for x, y in edges:
            if y not in parent:
                parent[y] = x
            else:
                candidates.append([parent[y], y])
                candidates.append([x, y])

        if candidates:
            # if edge make a cycle => it is answer
            # ex: [[2,1], [3,1], [4,2], [1,4]] => return [2, 1] because it makes a cycle
            # else if it don't make a cycle => return edge has added after(candidate[1)
            # ex: [[1,2], [1,3], [2,3]] => return [2, 3]
            if isCycle(candidates[0]):
                return candidates[0]
            return candidates[1]

        # if no edge has 2 parent => check edge make a cycle, using union-find
        # ex: [[1,2], [2,3], [3,4], [4,1], [1,5]] -> return [4, 1] because  because it makes a cycle
        for x, y in edges:
            if not union(x, y):
                return [x, y]
        return None


s = Solution()
# print(s.findRedundantDirectedConnection([[2, 1], [3, 1], [4, 2], [1, 4]]))
# print(s.findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]]))
print(s.findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]))
