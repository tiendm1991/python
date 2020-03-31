class Solution:
    def singleNonDuplicate(self, nums) -> int:
        def binarySearch(f, l):
            if f == l:
                return nums[f]
            m = (f + l) // 2
            if nums[m] > nums[m-1] and nums[m] < nums[m+1]:
                return nums[m]
            # number of half size
            n = m - f + 1
            if n % 2 == 0:
                if nums[m] == nums[m-1]:
                    return binarySearch(m+1, l)
                else:
                    return binarySearch(f, m-1)
            else:
                if nums[m] > nums[m-1]:
                    return binarySearch(m, l)
                else:
                    return binarySearch(f, m)
        return binarySearch(0, len(nums) - 1)