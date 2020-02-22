class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False
        checks = []
        for i in range(1, n-1):
            s1 = num[0:i]
            if s1[0] == '0' and len(s1) > 1:
                break
            x1 = int(s1)
            for j in range(i+1, n):
                s2 = num[i:j]
                if s2[0] == '0' and len(s2) > 1:
                    break
                x2 = int(s2)
                for k in range(j+1, n+1):
                    s3 = num[j:k]
                    if s3[0] == '0' and len(s3) > 1:
                        break
                    x3 = int(s3)
                    if x1 + x2 == x3:
                        a = [x2, x3, k]
                        while a[2] <= n:
                            if a[2] == n:
                                return True
                            x = a[0] + a[1]
                            s = str(x)
                            if num[a[2]:].startswith(s):
                                a = [a[1], x, a[2] + len(s)]
                            else:
                                break
        return False


s = Solution()
print(s.isAdditiveNumber('0235813'))
