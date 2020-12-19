import collections


class Solution:
    def movesToStamp(self, stamp: str, target: str):
        n = len(target)
        m = len(stamp)
        t = "*" * n
        stop = "*" * m

        def check(a, idx):
            for i in range(m):
                if a[idx + i] != '*' and a[idx + i] != stamp[i]:
                    return False
            return True

        visited = set()

        def backtrack(cur_str, cur_path):
            if cur_str in visited:
                return ""
            if cur_str == t:
                return cur_path
            candidate = set()
            for i in range(n - m + 1):
                if check(cur_str, i):
                    candidate.add(i)
            if candidate:
                next_str = cur_str
                next_path = cur_path
                for i in candidate:
                    if next_str[i: i + m] != stop:
                        next_str = next_str[:i] + stop + next_str[i + m:]
                        next_path += "-" + str(i)
                if next_str == cur_str:
                    visited.add(next_str)
                    return ""
                rx = backtrack(next_str, next_path)
                if rx:
                    return rx
                else:
                    visited.add(next_str)
                    return ""
            visited.add(cur_str)
            return ""

        r = backtrack(target, "")
        return [] if r == '' else [int(c) for c in r.strip("-").split("-")][::-1]


s = Solution()
print(s.movesToStamp("abc", "ababc"))
print(s.movesToStamp("abca", "aabcaca"))
print(s.movesToStamp("by", "bbybyybyby"))
# print(s.movesToStamp("qxq", "qxqxqxqqxqxqqxqxqxqqxqxqqqxqqxqqqxqqxxqxqqxqqqxqqq"))
# print(s.movesToStamp("o", "oooooooooo"))
# print(s.movesToStamp("aye", "eyeye"))
