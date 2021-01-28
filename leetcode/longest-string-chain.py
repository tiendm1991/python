class Solution:
    def longestStrChain(self, words) -> int:
        d = {i: {} for i in range(1, 17)}
        words.sort(key=lambda w: len(w))
        res = 1
        for w in words:
            n = len(w)
            if n == 1:
                d[1][w] = 1
                continue
            _max = 1
            for i in range(n):
                wCheck = w[:i] + w[i + 1:]
                if wCheck in d[n - 1]:
                    _max = max(_max, d[n - 1][wCheck] + 1)
            d[n][w] = _max
            res = max(res, _max)
        return res


s = Solution()
print(s.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
