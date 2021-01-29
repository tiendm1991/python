import collections


class Solution:
    def rearrangeBarcodes(self, a):
        n = len(a)
        res = [0] * n
        counter = collections.Counter(a)
        index = [0, 1]
        even = 0
        for k, v in sorted(counter.items(), key=lambda x: x[1], reverse=True):
            while v > 0:
                if index[even] >= n:
                    even = 1 - even
                res[index[even]] = k
                v -= 1
                index[even] += 2
        return res


s = Solution()
print(s.rearrangeBarcodes([7, 7, 7, 8, 5, 7, 5, 5, 5, 8]))
print(s.rearrangeBarcodes([1, 1, 1, 1, 2, 2, 3, 3]))
print(s.rearrangeBarcodes([1, 1, 1, 2, 2, 2]))
