class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0


s = Solution()
print(s.divisorGame(3))
print(s.divisorGame(15))
print(s.divisorGame(16))
