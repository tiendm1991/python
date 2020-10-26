class Solution:
    def processQueries(self, queries, m: int):
        d = {i + 1: i for i in range(m)}
        result = []
        for q in queries:
            idx = d[q]
            result.append(idx)
            for k in d:
                if k == q:
                    d[k] = 0
                elif d[k] < idx:
                    d[k] += 1
        return result


s = Solution()
print(s.processQueries([3, 1, 2, 1], 5))
