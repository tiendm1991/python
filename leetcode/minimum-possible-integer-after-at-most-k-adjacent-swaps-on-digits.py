class Solution:
    def minInteger(self, num: str, k: int) -> str:
        a = [int(c) for c in num]
        n = len(a)
        if k >= (n-1) * n // 2:
            return ''.join([str(x) for x in sorted(a)])

        def getIdxSwap(i, k):
            if i == n - 1:
                return -1
            minIdx = i
            for j in range(i + 1, min(i + k + 1, n)):
                if a[j] < a[minIdx]:
                    minIdx = j
            if a[minIdx] < a[i]:
                return minIdx
            return -1

        i = 0
        while i < n and k > 0:
            idx = getIdxSwap(i, k)
            if idx > -1:
                tmp = a[idx]
                for j in range(idx, i, -1):
                    a[j] = a[j-1]
                a[i] = tmp
                k -= idx - i
            i += 1

        return ''.join([str(x) for x in a])

s = Solution()
print(s.minInteger("9438957234785635408", 23))
