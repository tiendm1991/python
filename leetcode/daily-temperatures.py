class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        res = [0] * n
        stack = [0]
        for i in range(1, n):
            while stack and T[stack[-1]] < T[i]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res
