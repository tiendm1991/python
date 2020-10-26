class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        a = [c for c in dominoes]
        n = len(dominoes)
        dis = [n] * n
        r = -1
        for i in range(n):
            if a[i] == 'R':
                r = i
            elif a[i] == 'L':
                r = -1
            else:
                dis[i] = n if r == -1 else i - r
        l = -1
        for i in range(n - 1, -1, -1):
            if a[i] == 'L':
                l = i
            elif a[i] == 'R':
                l = -1
            else:
                x = n if l == -1 else l - i
                if x < dis[i]:
                    a[i] = 'L'
                elif x > dis[i]:
                    a[i] = 'R'
        return ''.join(a)


s = Solution()
print(s.pushDominoes(".L.R...LR..L.."))
