class Solution:
    def checkValidString2(self, s: str) -> bool:
        def valid(a):
            stack = []
            for c in a:
                if c == '(':
                    stack.append(c)
                elif c == ')':
                    if not stack or stack[-1] == ")":
                        return False
                    stack.pop()
            return len(stack) == 0
        def backtrack(a):
            if "*" not in a:
                return valid(a)
            idx = a.index("*")
            a[idx] = ""
            if backtrack(a):
                return True
            a[idx] = "("
            if backtrack(a):
                return True
            a[idx] = ")"
            if backtrack(a):
                return True
            a[idx] = "*"
            return False
        a = []
        for c in s:
            if c == "(" or c == "*":
                a.append(c)
            else:
                if a and a[-1] == "(":
                    a.pop()
                else:
                    a.append(c)
        return backtrack(a)

    def checkValidString(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return True
        dp = [[[-1 for i in range(n)] for j in range(n)] for k in range(n)]
        def check(a, i, nOpen, nClose):
            if i == len(a):
                return nOpen == nClose
            if dp[i][nOpen][nClose] != -1:
                return True if dp[i][nOpen][nClose] == 1 else False
            c = a[i]
            result = False
            if c == "(":
                result = check(a, i+1, nOpen+1, nClose)
            elif c == ")":
                if nClose == nOpen:
                    result = False
                else:
                    result = check(a, i + 1, nOpen, nClose + 1)
            else:
                result = check(a, i+1, nOpen, nClose) or check(a, i+1, nOpen+1, nClose) or (nClose < nOpen and check(a, i+1, nOpen, nClose+1))
            dp[i][nOpen][nClose] = result
            return result
        a = []
        for c in s:
            if c == "(" or c == "*":
                a.append(c)
            else:
                if a and a[-1] == "(":
                    a.pop()
                else:
                    a.append(c)
        return check(a, 0, 0, 0)

s = Solution()
print(s.checkValidString('*('))