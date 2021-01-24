class Solution:
    def minimumTeachings(self, n: int, languages, friendships) -> int:
        d = {i: set() for i in range(1, n + 1)}
        languages = [set(l) for l in languages]
        for i, u in enumerate(languages):
            for l in u:
                d[l].add(i)
        notConnect = []
        for i, f in enumerate(friendships):
            if len(languages[f[0] - 1] & languages[f[1] - 1]) == 0:
                notConnect.append([f[0] - 1, f[1] - 1])
        res = len(languages)
        for l in range(1, n + 1):
            c = 0
            for i, f in enumerate(notConnect):
                u1, u2 = f
                if u1 not in d[l]:
                    c += 1
                    d[l].add(u1)
                if u2 not in d[l]:
                    c += 1
                    d[l].add(u2)
            res = min(res, c)

        return res


s = Solution()
print(s.minimumTeachings(2,
                         [[2], [1], [2, 1], [1], [1, 2], [1], [2], [1], [1], [2], [1, 2], [1, 2], [1, 2], [2, 1], [1],
                          [2], [1, 2]],
                         [[15, 16], [4, 13], [3, 16], [5, 14], [1, 7], [2, 11], [3, 15], [4, 16], [7, 9], [6, 13],
                          [6, 16], [4, 10], [6, 9], [5, 6], [7, 12], [6, 12], [3, 7], [4, 7], [8, 10]]))
# print(s.minimumTeachings(17,
#                          [[4, 7, 2, 14, 6], [15, 13, 6, 3, 2, 7, 10, 8, 12, 4, 9], [16], [10], [10, 3],
#                           [4, 12, 8, 1, 16, 5, 15, 17, 13], [4, 13, 15, 8, 17, 3, 6, 14, 5, 10],
#                           [11, 4, 13, 8, 3, 14, 5, 7, 15, 6, 9, 17, 2, 16, 12], [4, 14, 6],
#                           [16, 17, 9, 3, 11, 14, 10, 12, 1, 8, 13, 4, 5, 6], [14], [7, 14],
#                           [17, 15, 10, 3, 2, 12, 16, 14, 1, 7, 9, 6, 4]],
#                          [[4, 11], [3, 5], [7, 10], [10, 12], [5, 7], [4, 5], [3, 8], [1, 5], [1, 6], [7, 8], [4, 12],
#                           [2, 4], [8, 9], [3, 10], [4, 7], [5, 12], [4, 9], [1, 4], [2, 8], [1, 2], [3, 4], [5, 10],
#                           [2, 7], [1, 7], [1, 8], [8, 10], [1, 9], [1, 10], [6, 7], [3, 7], [8, 12], [7, 9], [9, 11],
#                           [2, 5], [2, 3]]))
# print(s.minimumTeachings(2,
#                          [[1], [2], [1, 2]],
#                          [[1, 2], [1, 3], [2, 3]]))
# print(s.minimumTeachings(3,
#                          [[2], [1, 3], [1, 2], [3]],
#                          [[1, 4], [1, 2], [3, 4], [2, 3]]))