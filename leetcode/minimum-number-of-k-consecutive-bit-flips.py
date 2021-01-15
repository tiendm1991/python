import collections


class Solution:
    def minKBitFlips_Onk(self, a, k) -> int:
        n = len(a)
        res = 0
        for i in range(n):
            if a[i] == 1:
                continue
            if i + k > n:
                return -1
            for j in range(i, i + k):
                a[j] ^= 1
            res += 1
        return res

    def minKBitFlips_maskbit(self, a, k) -> int:
        n = len(a)
        res = 0
        cur = 0
        for i in range(k):
            cur = (cur << 1) | a[i]
        for i in range(n):
            mask = (1 << min(k, n - i)) - 1
            check = 1 << min(k, n - i) - 1
            x = cur & check
            if not x:
                if i + k > n:
                    return -1
                cur ^= mask
                res += 1
            cur &= check ^ mask
            if i + k < n:
                cur = (cur << 1) | a[i + k]
        return res

    def minKBitFlips(self, a, k) -> int:
        n = len(a)
        res = 0
        q = collections.deque()
        flip = 0
        for i in range(n):
            if a[i] ^ (flip & 1) == 0:
                if i + k > n:
                    return -1
                q.append(i + k - 1)
                res += 1
                flip += 1
            if q and i >= q[0]:
                q.popleft()
                flip -= 1
        return res


s = Solution()
print(s.minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3))
print(s.minKBitFlips([0, 1, 1], 2))
print(s.minKBitFlips([1, 1], 2))
print(s.minKBitFlips([0, 1, 0], 1))
print(s.minKBitFlips([1, 1, 0], 2))
