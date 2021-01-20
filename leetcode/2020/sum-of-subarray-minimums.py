class Solution:
    def sumSubarrayMins1(self, arr) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        res = 0
        left, right, stack = [0] * n, [0] * n, []
        for i, x in enumerate(arr):
            count = 0
            while stack and stack[-1][0] >= x:
                count += stack.pop()[1] + 1
            left[i] = count
            stack.append([x, count])
        stack = []
        for i in range(n - 1, -1, -1):
            x = arr[i]
            count = 0
            while stack and stack[-1][0] > x:
                count += stack.pop()[1] + 1
            right[i] = count
            stack.append([x, count])
        for i in range(n):
            x, y = left[i], right[i]
            res = (res + arr[i] * (x * y + x + y + 1)) % mod
        return res

    def sumSubarrayMins(self, arr) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        res = 0
        left, right, stack = [0] * n, [0] * n, []
        for i, x in enumerate(arr):
            count = 1
            while stack and stack[-1][0] >= x:
                count += stack.pop()[1]
            left[i] = count
            stack.append([x, count])
        stack = []
        for i in range(n - 1, -1, -1):
            x = arr[i]
            count = 1
            while stack and stack[-1][0] > x:
                count += stack.pop()[1]
            right[i] = count
            stack.append([x, count])
        for i in range(n):
            x, y = left[i], right[i]
            res = (res + arr[i] * x * y) % mod
        return res


s = Solution()
print(s.sumSubarrayMins([5, 6, 5]), s.sumSubarrayMins1([5, 6, 5]))
print(s.sumSubarrayMins([7, 5, 8, 5]), s.sumSubarrayMins1([7, 5, 8, 5]))
print(s.sumSubarrayMins([71, 55, 82, 55]), s.sumSubarrayMins1([71, 55, 82, 55]))
print(s.sumSubarrayMins([3, 1, 2, 4]), s.sumSubarrayMins1([3, 1, 2, 4]))
print(s.sumSubarrayMins([1, 5, 3, 9, 7, 2, 5, 6]), s.sumSubarrayMins1([1, 5, 3, 9, 7, 2, 5, 6]))
