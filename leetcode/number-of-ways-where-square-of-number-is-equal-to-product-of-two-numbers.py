class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        d, d2 = {}, {}
        for j in range(n2-1):
            for k in range(j+1, n2):
                m = nums2[j] * nums2[k]
                if m in d:
                    d[m].append((j, k))
                else:
                    d[m] = [(j, k)]
        for j in range(n1-1):
            for k in range(j+1, n1):
                m = nums1[j] * nums1[k]
                if m in d2:
                    d2[m].append((j, k))
                else:
                    d2[m] = [(j, k)]
        ans = 0
        for i, x in enumerate(nums1):
            if x ** 2 in d:
                ans += len(d[x **2])
        for i, x in enumerate(nums2):
            if x ** 2 in d2:
                ans += len(d2[x **2])
        return ans