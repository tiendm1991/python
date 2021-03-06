class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        arr = [int(c) for c in s]
        n = len(arr)

        def add(ar):
            return [(ar[i] + a) % 10 if i % 2 == 1 else ar[i] for i in range(n)]

        def rotate(ar):
            return ar[n - b:] + ar[:n - b]

        def toString(ar):
            return ''.join([str(c) for c in ar])

        def bfs():
            visited = {s}
            ans = s
            q = [arr]
            while q:
                newQ = []
                for e in q:
                    newAdd = add(e)
                    newRot = rotate(e)
                    newSAdd = toString(newAdd)
                    newSRot = toString(newRot)
                    ans = min(ans, newSAdd, newSRot)
                    if newSAdd not in visited:
                        visited.add(newSAdd)
                        newQ.append(newAdd)
                    if newSRot not in visited:
                        visited.add(newSRot)
                        newQ.append(newRot)
                q = newQ
            return ans

        def dfs(cur, visited):
            ans = toString(cur)
            visited.add(ans)
            newAdd = add(cur)
            newRot = rotate(cur)
            newSAdd = toString(newAdd)
            newSRot = toString(newRot)
            if newSAdd not in visited:
                ans = min(ans, dfs(newAdd, visited))
            if newSRot not in visited:
                ans = min(ans, dfs(newRot, visited))
            return ans

        return dfs(arr, set())


s = Solution()
print(s.findLexSmallestString("43987654", 7, 3))
# print(s.findLexSmallestString("0011", 4, 2))
# print(s.findLexSmallestString("74", 5, 1))
print(s.findLexSmallestString("5525", 9, 2))
