class Solution:
    def modifyString(self, s: str) -> str:
        n = len(s)
        chars = 'abcdefghijklmnopqrstuvwxyz'
        a = [c for c in s]
        for i, c in enumerate(s):
            if c != '?':
                continue
            if i == 0:
                a[0] = 'a'
                if s[1] == 'a':
                    a[0] = 'b'
                continue
            for ch in chars:
                if ch == a[i - 1] or (i < n - 1 and ch == a[i + 1]):
                    continue
                a[i] = ch
                break
        return ''.join(a)


s = Solution()
print(s.modifyString('??yw?ipkj?'))
