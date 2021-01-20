class Solution:
    def findReplaceString(self, s: str, indexes, sources, targets) -> str:
        n = len(indexes)
        input = [[indexes[i], sources[i], targets[i]] for i in range(n)]
        input.sort(reverse=True)
        a = [c for c in s]
        for i in range(n):
            if s[input[i][0]:].startswith(input[i][1]):
                a[input[i][0]: input[i][0] + len(input[i][1])] = [c for c in input[i][2]]
        return ''.join(a)


s = Solution()
print(s.findReplaceString("vmokgggqzp",
                          [3, 5, 1],
                          ["kg", "ggq", "mo"],
                          ["s", "so", "bfr"]))
