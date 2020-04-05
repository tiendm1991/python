import collections
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def build(s, ca, cb, cc):
            x, y, z = a-ca, b -cb, c - cc
            _max = max(x,y,z)
            if _max == x:
                if ca < a and s[-2:] != 'aa':
                    return build(s + 'a', ca+1, cb, cc)
                elif y >= z:
                    if cb < b and s[-2:] != 'bb':
                        return build(s + 'b', ca, cb + 1, cc)
                elif cc < c and s[-2:] != 'cc':
                    return build(s + 'c', ca, cb, cc+1)
            if _max == y:
                if cb < b and s[-2:] != 'bb':
                    return build(s + 'b', ca, cb + 1, cc)
                elif x >= z:
                    if ca < a and s[-2:] != 'aa':
                        return build(s + 'a', ca + 1, cb, cc)
                elif cc < c and s[-2:] != 'cc':
                    return build(s + 'c', ca, cb, cc+1)
            if _max == z:
                if cc < c and s[-2:] != 'cc':
                    return build(s + 'c', ca, cb, cc+1)
                elif x >= y:
                    if ca < a and s[-2:] != 'aa':
                        return build(s + 'a', ca + 1, cb, cc)
                elif cb < b and s[-2:] != 'bb':
                    return build(s + 'b', ca, cb + 1, cc)
            return s
        return build('', 0, 0, 0)
s = Solution()
print(s.longestDiverseString(5,4,3))