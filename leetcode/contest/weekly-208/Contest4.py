# https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/submissions/
class Solution:
    def maximumRequests1(self, n: int, requests) -> int:
        ans = [0, 0]
        rq = []
        count = [0] * n
        for f, t in requests:
            if f == t:
                ans[0] += 1
            else:
                rq.append([f, t])
                count[f] += 1
        l = len(rq)

        def help(mask):
            check = count[::]
            countRq = 0
            for i in range(l):
                if mask & (1 << i):
                    check[rq[i][0]] -= 1
                    check[rq[i][1]] += 1
                    countRq += 1
            if check != count:
                countRq = 0
            return countRq

        for i in range(1 << l):
            ans[1] = max(ans[1], help(i))
        return ans[0] + ans[1]

    def maximumRequests(self, n: int, requests) -> int:
        ans = [0, 0]
        rq = []
        count = [0] * n
        for f, t in requests:
            if f == t:
                ans[0] += 1
            else:
                rq.append([f, t])
                count[f] += 1
        l = len(rq)

        def backtrack(c, countRq, start):
            if c == count:
                ans[1] = max(ans[1], countRq)
            for i in range(start, l):
                c[rq[i][0]] -= 1
                c[rq[i][1]] += 1
                backtrack(c, countRq + 1, i + 1)
                c[rq[i][0]] += 1
                c[rq[i][1]] -= 1

        backtrack(count[::], 0, 0)

        return ans[0] + ans[1]


s = Solution()
print(s.maximumRequests(5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]))
print(s.maximumRequests(4,
                        [[0, 0], [1, 3], [1, 3], [2, 3], [1, 0], [2, 2], [1, 2], [2, 1], [1, 3], [0, 2], [3, 0], [3, 1],
                         [2, 2], [3, 0], [0, 3], [3, 1]]))
