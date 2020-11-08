class Solution:
    def canFormArray1(self, arr, pieces) -> bool:
        n = len(pieces)

        def help(i, visited):
            if i >= len(arr):
                return True
            for j in range(n):
                if visited[j]:
                    continue
                if pieces[j] == arr[i: i + len(pieces[j])]:
                    visited[j] = True
                    if help(i + len(pieces[j]), visited):
                        return True
                    visited[j] = False
            return False

        return help(0, [False] * n)

    def canFormArray(self, arr, pieces) -> bool:
        d = {p[0]: p for p in pieces}
        check = []
        for x in arr:
            check += d.get(x, [])
        return check == arr


s = Solution()
print(s.canFormArray([91, 4, 64, 78], [[78], [4, 64], [91]]))
