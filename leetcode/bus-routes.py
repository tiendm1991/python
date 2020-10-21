import queue


class Solution:
    def numBusesToDestination2(self, routes, s: int, t: int) -> int:
        n = len(routes)
        if s == t:
            return 0
        if n == 1:
            return 1 if s in routes[0] and t in routes[0] else -1
        rs = [set(r) for r in routes]
        edges = {i: set() for i in range(n)}
        for i in range(n - 1):
            for j in range(i + 1, n):
                for v in rs[i]:
                    if v in rs[j]:
                        edges[i].add(j)
                        edges[j].add(i)
                        break
        q = [i for i in range(n) if s in rs[i]]
        visited = [False] * n
        for i in q:
            visited[i] = True
        ans = 0
        while q:
            newQ = []
            ans += 1
            for i in q:
                if t in rs[i]:
                    return ans
                for j in edges[i]:
                    if not visited[j]:
                        visited[j] = True
                        newQ.append(j)
            q = newQ
        return -1

    def numBusesToDestination(self, routes, s: int, t: int) -> int:
        n = len(routes)
        if s == t:
            return 0
        if n == 1:
            return 1 if s in routes[0] and t in routes[0] else -1
        rs = [set(r) for r in routes]
        edges = {i: set() for i in range(n)}
        for i in range(n - 1):
            for j in range(i + 1, n):
                for v in rs[i]:
                    if v in rs[j]:
                        edges[i].add(j)
                        edges[j].add(i)
                        break
        q = queue.Queue()
        visited = [False] * n
        for i in range(n):
            if s in rs[i]:
                q.put((i, 1))
                visited[i] = True
        while not q.empty():
            v, length = q.get()
            if t in rs[v]:
                return length
            for j in edges[v]:
                if not visited[j]:
                    visited[j] = True
                    q.put((j, length + 1))
        return -1


s = Solution()
print(s.numBusesToDestination([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12))
print(s.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6))
print(s.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 7, 6))
