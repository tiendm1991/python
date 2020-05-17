class Solution:
    def peopleIndexes(self, favoriteCompanies):
        # f = sorted(favoriteCompanies, key=lambda x : len(x), reverse=True)
        f = [set(x) for x in favoriteCompanies]
        n = len(f)
        result = []
        for i in range(n):
            valid = True
            for j in range(n):
                if i != j and f[i].issubset(f[j]):
                    valid = False
                    break
            if valid:
                result.append(i)
        return result

s = Solution()
print(s.peopleIndexes())
