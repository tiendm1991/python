class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        n = len(s)
        if n == 1:
            return s
        if k > 1:
            return ''.join(sorted(s))
        s2 = 2 * s
        res = "z" * n
        for i in range(n):
            tmp = s2[i: i + n]
            if tmp < res:
                res = tmp
        return res


s = Solution()
print(s.orderlyQueue("cba", 1))
print(s.orderlyQueue("baaca", 1))
print(s.orderlyQueue("baacaab", 1))
