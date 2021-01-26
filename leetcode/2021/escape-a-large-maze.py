import collections


class Solution:
    def isEscapePossible(self, blocked, source, target) -> bool:
        n = 10 ** 6
        direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        blocked = {tuple(b) for b in blocked}
        q = collections.deque()
        q.append(source)
        visited = {tuple(b) for b in blocked}
        visited.add(tuple(source))
        while q:
            x, y = q.popleft()
            if [x, y] == target:
                return True
            for d in direct:
                if 0 <= x + d[0] < n and 0 <= y + d[1] < n and (x + d[0], y + d[1]) not in visited:
                    q.append([x + d[0], y + d[1]])
                    visited.add((x + d[0], y + d[1]))
        return False


s = Solution()
print(s.isEscapePossible([[0, 1], [1, 0]], [0, 0], [0, 2]))
