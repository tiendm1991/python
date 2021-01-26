import collections


class Solution:
    def isEscapePossible(self, blocked, source, target) -> bool:
        n = 10 ** 6
        direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bfs(s, t):
            q = collections.deque()
            q.append(s)
            visited = {tuple(b) for b in blocked}
            visited.add(tuple(s))
            count = 1
            while q:
                x, y = q.popleft()
                if [x, y] == t:
                    return True
                for d in direct:
                    if 0 <= x + d[0] < n and 0 <= y + d[1] < n and (x + d[0], y + d[1]) not in visited:
                        q.append([x + d[0], y + d[1]])
                        visited.add((x + d[0], y + d[1]))
                if len(q) + count >= 20000:
                    return True
                count += 1
            return False

        return bfs(source, target) and bfs(target, source)


s = Solution()
print(s.isEscapePossible([[0, 1],
                          [1, 0]], [0, 0], [0, 2]))
