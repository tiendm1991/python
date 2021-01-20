class Solution:
    def canReach(self, arr, start: int) -> bool:
        n = len(arr)
        q = [start]
        visited = {start}
        while q:
            newQ = []
            for i in q:
                if arr[i] == 0:
                    return True
                j, k = i + arr[i], i - arr[i]
                if j < n and j not in visited:
                    visited.add(j)
                    newQ.append(j)
                if k >= 0 and k not in visited:
                    visited.add(k)
                    newQ.append(k)
            q = newQ
        return False


s = Solution()
print(s.canReach([3, 0, 2, 1, 2], 2))
# print(s.canReach([4, 2, 3, 0, 3, 1, 2], 5))
