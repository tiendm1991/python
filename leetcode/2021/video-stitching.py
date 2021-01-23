import functools


class Solution:
    def videoStitching(self, clips, t: int) -> int:
        def compare(c1, c2):
            if c1[0] != c2[0]:
                return c1[0] - c2[0]
            return c1[1] - c2[1]

        a = sorted(clips, key=functools.cmp_to_key(compare))
        if a[0][0] > 0 or a[-1][1] < t:
            return -1
        res = [a[0]]
        for i in range(1, len(a)):
            if res[-1][0] <= a[i][0] and a[i][1] <= res[-1][1]:
                continue
            elif a[i][0] == res[-1][0]:
                res[-1][1] = a[i][1]
            elif a[i][0] > res[-1][1]:
                return -1
            else:
                res.append(a[i])
                if a[i][1] >= t:
                    break
        return len(res)


s = Solution()
# print(s.videoStitching([[0, 2], [1, 6], [3, 10]], 10))
# print(s.videoStitching([[0, 2], [4, 8]], 5))
# print(s.videoStitching([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10))
print(s.videoStitching(
    [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5],
     [5, 7], [6, 9]], 9))
