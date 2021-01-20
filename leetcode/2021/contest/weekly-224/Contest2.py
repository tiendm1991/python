class Solution:
    def tupleSameProduct(self, nums) -> int:
        d = {}
        n = len(nums)
        if n < 4:
            return 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                x = nums[i] * nums[j]
                if x not in d:
                    d[x] = [(i, j)]
                else:
                    d[x].append((i, j))
        res = 0
        for k, v in d.items():
            nv = len(v)
            if nv < 2:
                continue
            for i in range(nv - 1):
                a, b = v[i]
                for j in range(i + 1, nv):
                    c, d = v[j]
                    if a != b != c != d:
                        res += 8
        return res


s = Solution()
print(s.tupleSameProduct([1, 2, 4, 5, 10]))
print(s.tupleSameProduct([2, 3, 4, 6, 8, 12]))
