class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        depth = 0
        ans = 0
        for c in s:
            if c == "(":
                depth += 1
                if depth > ans:
                    ans = depth
            elif c == ")":
                depth -= 1
        return ans