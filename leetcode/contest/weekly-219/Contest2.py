class Solution:
    def minPartitions(self, n: str) -> int:
        return max([int(x) for x in n])


s = Solution()
print(s.minPartitions("82734"))
print(s.minPartitions("32"))
