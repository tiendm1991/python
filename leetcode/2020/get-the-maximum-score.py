# https://leetcode.com/contest/weekly-contest-200/problems/get-the-maximum-score/
class Solution:
    def maxSum(self, nums1, nums2) -> int:
        mod = 10 ** 9 + 7

        def getPrefix(a):
            pre = [0] * (len(a) + 1)
            for k in range(1, len(a) + 1):
                pre[k] = pre[k - 1] + a[k - 1]
            return pre

        n1, n2 = len(nums1), len(nums2)
        a1, a2 = [0], [0]
        i, j = 0, 0
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                a1.append(i + 1)
                a2.append(j + 1)
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        a1.append(n1)
        a2.append(n2)
        p1, p2 = getPrefix(nums1), getPrefix(nums2)
        ans = 0
        for i in range(1, len(a1)):
            ans = (ans + max(p1[a1[i]] - p1[a1[i - 1]], p2[a2[i]] - p2[a2[i - 1]])) % mod
        return ans


s = Solution()
print(s.maxSum([2, 4, 5, 8, 10], [4, 6, 8, 9]))
print(s.maxSum([1, 4, 5, 8, 9, 11, 19], [2, 3, 4, 11, 12]))
