import functools


class Solution:
    def videoStitching(self, clips, t: int) -> int:
        if t == 0:
            return 0

        def compare(c1, c2):
            if c1[0] != c2[0]:
                return c1[0] - c2[0]
            return c1[1] - c2[1]

        b = sorted(clips, key=functools.cmp_to_key(compare))
        if b[0][0] > 0 or b[-1][1] < t:
            return -1
        a = [[b[0][0], b[0][1]]]
        for i in range(1, len(b)):
            if b[i][0] == a[-1][0]:
                a[-1][1] = b[i][1]
            else:
                a.append(b[i][::])
        end = a[0][1]
        res = 1
        i = 1
        while i < len(a):
            if end >= t:
                break
            j = i
            endTmp = end
            while j < len(a) and a[j][0] <= end:
                endTmp = max(endTmp, a[j][1])
                j += 1
            if j == i:
                return -1
            res += 1
            end = endTmp
            i = j
        return res


s = Solution()
print(s.videoStitching([[16, 18], [16, 20], [3, 13], [1, 18], [0, 8], [5, 6], [13, 17], [3, 17], [5, 6]], 15))
print(s.videoStitching([[5, 7], [1, 8], [0, 0], [2, 3], [4, 5], [0, 6], [5, 10], [7, 10]], 5))
print(s.videoStitching([[0, 2], [3, 10], [8, 10], [1, 9], [1, 5], [5, 9]], 10))
print(s.videoStitching([[0, 2], [1, 6], [3, 10]], 10))
print(s.videoStitching([[0, 2], [4, 8]], 5))
print(s.videoStitching([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10))
print(s.videoStitching(
    [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5],
     [5, 7], [6, 9]], 9))
