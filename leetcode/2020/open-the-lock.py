class Solution:
    def openLock(self, deadends, target: str) -> int:
        if target == "0000":
            return 0
        visited = {w for w in deadends}
        if "0000" in visited:
            return -1
        q = ["0000"]
        visited.add("0000")
        ans = 0
        while q:
            newQ = []
            ans += 1
            for x in q:
                a = [int(c) for c in x]
                for i in range(4):
                    tmp = a[i]
                    a[i] = (tmp + 1) % 10
                    s1 = f'{a[0]}{a[1]}{a[2]}{a[3]}'
                    a[i] = (tmp + 9) % 10
                    s2 = f'{a[0]}{a[1]}{a[2]}{a[3]}'
                    a[i] = tmp
                    if s1 == target or s2 == target:
                        return ans
                    if s1 not in visited:
                        newQ.append(s1)
                        visited.add(s1)
                    if s2 not in visited:
                        newQ.append(s2)
                        visited.add(s2)
            q = newQ
        return -1


s = Solution()
print(s.openLock(["0000"], "8888"))
print(s.openLock(["0000"], "8888"))
