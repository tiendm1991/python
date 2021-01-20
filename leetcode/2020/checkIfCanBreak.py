import collections


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        a1 = sorted([c for c in s1])
        a2 = sorted([c for c in s2])
        check = 0
        for i in range(len(a1)):
            if a1[i] == a2[i]:
                continue
            if check == 0:
                check = 1 if a1[i] > a2[i] else -1
            else:
                check2 = 1 if a1[i] > a2[i] else -1
                if check * check2 == -1:
                    return False
        return True


s = Solution()
print(s.checkIfCanBreak('abe', 'acd'))
