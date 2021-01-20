class Solution:
    def maxNumOfSubstrings(self, s: str):
        d = {}
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        d_search = {x: [] for x in alpha}
        visited = {x: False for x in alpha}
        for i, c in enumerate(s):
            if c not in d:
                d[c] = [i, i]
            else:
                d[c][1] = i
            d_search[c].append(i)

        def biSearch(arr, l, h, x, y):
            if l > h or x > arr[h] or y < arr[l] or x > y:
                return False
            m = (l + h) // 2
            if x <= arr[m] <= y:
                return True
            if arr[m] > y:
                return biSearch(arr, l, m - 1, x, y)
            if arr[m] < x:
                return biSearch(arr, m + 1, h, x, y)
            return False

        i = 0
        while i < 26:
            c = alpha[i]
            if c not in d or visited[c]:
                i += 1
                continue
            r = d[c]
            repeat = False
            for c2 in alpha:
                if c2 not in d or c2 == c:
                    continue
                r2 = d[c2]
                if r[1] < r2[0] or r[0] > r2[1]:
                    continue
                arr = d_search[c2]
                if not biSearch(arr, 0, len(arr) - 1, r[0] + 1, r[1] - 1):
                    continue
                r3 = [min(r[0], r2[0]), max(r[1], r2[1])]
                if r != r3:
                    d[c] = r3
                    repeat = True
                    break
            if not repeat:
                visited[c] = True
                i += 1

        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1][1])}
        cur = None
        ans = []
        for k in d:
            if not cur or d[k][0] >= cur[1]:
                cur = d[k]
                ans.append(s[cur[0]:cur[1] + 1])
            if cur[1] == len(s) - 1:
                break
        return ans


s = Solution()
print(s.maxNumOfSubstrings("dedbeaccbb"))
print(s.maxNumOfSubstrings("dbcaacadacd"))
