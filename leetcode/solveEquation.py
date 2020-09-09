class Solution:
    def solveEquation(self, equation: str) -> str:
        equation = equation.split("=")
        left = equation[0]
        right = equation[1]
        left = left.replace("-", "+-")
        if left[0] == '+':
            left = left[1:]
        right = right.replace("-", "+-")
        if right[0] == '+':
            right = right[1:]
        left = left.split("+")
        right = right.split("+")
        x, v = 0, 0
        for e in left:
            if 'x' in e:
                x += 1 if len(e) == 1 else -1 if len(e) == 2 and e[0] == '-' else int(e[:-1])
            else:
                v -= int(e)
        for e in right:
            if 'x' in e:
                x -= 1 if len(e) == 1 else -1 if len(e) == 2 and e[0] == '-' else int(e[:-1])
            else:
                v += int(e)
        if x == 0:
            if v == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        return f'x={v // x}'


s = Solution()
print(s.solveEquation("x=-x"))
