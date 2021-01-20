class Solution:
    def shortestPathAllKeys(self, a) -> int:
        keys = 'abcdefghijklmnopqrstuvwxyz'
        locks = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        dictKey = {keys[i]: i for i in range(26)}
        dictLock = {locks[i]: i for i in range(26)}
        direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n, k, x, y = len(a), len(a[0]), 0, 0, 0
        for i in range(m):
            for j in range(n):
                if a[i][j] == '@':
                    x, y = i, j
                elif a[i][j] in keys:
                    k += 1
        target = (1 << k) - 1
        q = [(x, y, 0)]
        visited = {(x, y, 0)}
        ans = 0
        while q:
            newQ = []
            for x1, y1, mask in q:
                if mask == target:
                    return ans
                for d in direct:
                    i, j = x1 + d[0], y1 + d[1]
                    if 0 <= i < m and 0 <= j < n and a[i][j] != '#':
                        if a[i][j] in dictKey:
                            newMask = mask | (1 << dictKey[a[i][j]])
                            if (i, j, newMask) not in visited:
                                newQ.append((i, j, newMask))
                                visited.add((i, j, newMask))
                        elif (i, j, mask) not in visited and (
                                a[i][j] not in dictLock or mask & (1 << dictLock[a[i][j]])):
                            newQ.append((i, j, mask))
                            visited.add((i, j, mask))
            ans += 1
            q = newQ
        return -1


s = Solution()
print(s.shortestPathAllKeys(["@..aA",
                             "..B#.",
                             "....b"]))
print(s.shortestPathAllKeys(["@.a.#",
                             "###.#",
                             "b.A.B"]))
