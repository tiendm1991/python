from  datetime import datetime
import functools
import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        def short(x, y):
            a, b = abs(x), abs(y)
            gcd = math.gcd(a, b)
            return [x // gcd, y // gcd]

        def format(x):
            sign = "-" if x[0] * x[1] < 0 else ""
            return sign + "{}/{}".format(abs(x[0]), abs(x[1]))

        def add(a, b):
            return short(a[0] * b[1] + a[1] * b[0], a[1] * b[1])

        expression = expression.replace("-", "+-")
        expression = "0/1+" + expression
        expression = expression.replace("++", "+")
        exp_arr = []
        for s in expression.split("+"):
            arr = s.split("/")
            frac = [int(arr[0]), int(arr[1])]
            exp_arr.append(frac)
        result = functools.reduce(lambda a, b: add(a, b), exp_arr)
        return format(result)
s = Solution()
startTime = datetime.now()
print(s.fractionAddition("5/3+1/3"))
print(datetime.now() - startTime)