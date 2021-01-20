class Solution:
    def intersectionSizeTwo(self, intervals) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        a = []
        i = 0
        while i < len(intervals):
            if not a or intervals[i][0] > a[-1][0]:
                a.append(intervals[i])
            i += 1
        ans = set()
        pre = [-1, -1]
        for x in a:
            if pre[1] < x[0]:
                ans.add(x[1])
                ans.add(x[1] - 1)
                pre = [x[1] - 1, x[1]]
            elif pre[0] < x[0]:
                check = x[1]
                while check >= x[0] and check in ans:
                    check -= 1
                ans.add(check)
                pre = [min(pre[1], check), max(pre[1], check)]
        return len(ans)


s = Solution()
print(s.intersectionSizeTwo([[0, 1], [1, 4], [2, 6], [4, 7], [5, 8], [7, 8]]))
print(s.intersectionSizeTwo([[4, 7], [4, 14], [7, 14], [6, 17], [14, 21]]))
print(s.intersectionSizeTwo([[1, 2], [2, 3], [2, 4], [5, 6]]))
