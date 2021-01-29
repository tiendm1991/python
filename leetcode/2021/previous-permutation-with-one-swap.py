class Solution:
    def prevPermOpt1(self, a):
        n = len(a)
        if n == 1:
            return a
        j, i = n - 1, n - 2
        indexes = [j]
        while i >= 0:
            if a[i] > a[i + 1]:
                break
            elif a[i] == a[i + 1]:
                indexes[-1] = i
            else:
                indexes.append(i)
            i -= 1
        if i == -1:
            return a
        for idx in indexes:
            if a[idx] < a[i]:
                a[i], a[idx] = a[idx], a[i]
                break
        return a


s = Solution()
print(s.prevPermOpt1([3, 1, 1, 3]))
print(s.prevPermOpt1([1, 9, 4, 6, 7]))
print(s.prevPermOpt1([3, 2, 1]))
