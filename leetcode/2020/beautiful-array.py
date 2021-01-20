class Solution:
    def beautifulArray(self, N: int):
        def helper(a):
            n = len(a)
            if n <= 2:
                return a
            odd = [a[i] for i in range(n) if i % 2 == 0]
            even = [a[i] for i in range(n) if i % 2 == 1]
            return helper(odd) + helper(even)

        return helper([i for i in range(1, N + 1)])


s = Solution()
print(s.beautifulArray(4))  # [2,1,4,3]
print(s.beautifulArray(5))  # [3,1,2,5,4]
print(s.beautifulArray(6))  # [1,5,3,2,6,4]
