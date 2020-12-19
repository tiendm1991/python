import collections


class Solution:
    def movesToStamp_backtrack(self, stamp: str, target: str):
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
            candidates = set()
            for i in range(n - m + 1):
                if check(cur_str, i):
                    candidates.add(i)
            if candidates:
                next_str = cur_str
                next_path = cur_path
                for i in candidates:
                    if next_str[i: i + m] != stop:
                        next_str = next_str[:i] + stop + next_str[i + m:]
                        next_path += "-" + str(i)
                if next_str == cur_str:
                    visited.add(next_str)
                    return ""
                rx = backtrack(next_str, next_path)
                if rx != "":
                    return rx
                else:
                    visited.add(next_str)
                    return ""
            visited.add(cur_str)
            return ""

        r = backtrack(target, "")
        return [] if r == '' else [int(c) for c in r.strip("-").split("-")][::-1]

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

        pre_str = ''
        cur_str, cur_path = target, []
        while True:
            if cur_str == t:
                break
            if cur_str == pre_str:
                return []
            pre_str = cur_str  # to check loop inf
            candidates = set()
            for i in range(n - m + 1):
                if check(cur_str, i):
                    candidates.add(i)
            if candidates:
                next_str, next_path = cur_str, cur_path
                for i in candidates:
                    if next_str[i: i + m] != stop:
                        next_str = next_str[:i] + stop + next_str[i + m:]
                        next_path += [i]
                cur_str, cur_path = next_str, next_path
        return cur_path[::-1]


s = Solution()
print(s.movesToStamp("abca", "aabcaca"))
print(s.movesToStamp("abc", "ababc"))
print(s.movesToStamp("by", "bbybyybyby"))
print(s.movesToStamp("qxq", "qxqxqxqqxqxqqxqxqxqqxqxqqqxqqxqqqxqqxxqxqqxqqqxqqq"))
print(s.movesToStamp("o", "oooooooooo"))
print(s.movesToStamp("aye", "eyeye"))
