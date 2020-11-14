class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        n = len(A)
        if n == 1:
            return 0
        visited = {A}
        q = [A]
        ans = 0
        while q:
            newQ = []
            for s in q:
                if s == B:
                    return ans
                a = [c for c in s]
                i = 0
                while i < n and a[i] == B[i]:
                    i += 1
                for j in range(i + 1, n):
                    if a[j] != B[i]:
                        continue
                    a[i], a[j] = a[j], a[i]
                    newS = ''.join(a)
                    if newS not in visited:
                        newQ.append(newS)
                        visited.add(newS)
            q = newQ
            ans += 1
        return -1


s = Solution()
print(s.kSimilarity("aabc", "abca"))
print(s.kSimilarity("abc", "bca"))
