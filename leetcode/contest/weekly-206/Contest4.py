# https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        a = [int(c) for c in s]
        b = [int(c) for c in t]
        idx = {i: [] for i in range(10)}
        pos = [0] * 10
        for i, num in enumerate(a):
            idx[num].append(i)
        for i, num in enumerate(b):
            if not idx[num]:
                return False
            if pos[num] >= len(idx[num]):
                return False
            cur_idx = idx[num][pos[num]]
            for j in range(num):
                if pos[j] < len(idx[j]) and idx[j][pos[j]] < cur_idx:
                    return False
            pos[num] += 1
        return True


s = Solution()
print(s.isTransformable("84532", "34852"))
