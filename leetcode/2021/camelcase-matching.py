import string


class Solution:
    def camelMatch(self, queries, pattern: str):
        def check(w):
            i, j = 0, 0
            while i < len(pattern):
                if j == len(w):
                    break
                while j < len(w) and w[j] != pattern[i]:
                    if w[j] not in string.ascii_lowercase:
                        return False
                    j += 1
                if j < len(w):
                    i += 1
                    j += 1
            if i < len(pattern):
                return False
            while j < len(w):
                if w[j] not in string.ascii_lowercase:
                    return False
                j += 1
            return True

        n = len(queries)
        res = [False] * n
        for idx, q in enumerate(queries):
            res[idx] = check(q)
        return res


s = Solution()
print(s.camelMatch(["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FoBaT"))
