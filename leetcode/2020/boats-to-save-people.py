class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        people.sort()
        ans = 0
        i, j = 0, len(people) - 1
        while i < j:
            if people[i] + people[j] <= limit:
                ans += 1
                i += 1
                j -= 1
            else:
                ans += 1
                j -= 1
        if i == j:
            ans += 1
        return ans


s = Solution()
print(s.numRescueBoats([3, 2, 2, 1], 3))
