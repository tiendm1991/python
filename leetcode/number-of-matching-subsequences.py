import string


class Solution:
    def numMatchingSubseq(self, S: str, words) -> int:
        d = {c: [] for c in string.ascii_lowercase}
        for i, c in enumerate(S):
            d[c].append(i)

        def valid(word):
            minIdx = -1
            for c in word:
                idx = d[c]
                if len(idx) == 0 or idx[-1] <= minIdx:
                    return False
                l, r = 0, len(idx) - 1
                while l <= r:
                    if idx[l] > minIdx:
                        minIdx = idx[l]
                        break
                    m = (l + r) // 2
                    if idx[m] <= minIdx:
                        l = m + 1
                    else:
                        r = m
            return True

        ans = 0
        for w in words:
            if valid(w):
                ans += 1
        return ans


s = Solution()
print(s.numMatchingSubseq("kvbnnuglnagtvamxkqtuvabjrikfwronbrdyyjn", ["kvbnnugln"]))
