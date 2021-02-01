# https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k = n - 1
        while k > 0:
            if nums[k] > nums[k - 1]:
                break
            k -= 1
        if k == 0:
            reverse(0, n - 1)
        else:
            i = n - 1
            while i >= k:
                if nums[i] > nums[k - 1]:
                    break
                i -= 1
            nums[i], nums[k - 1] = nums[k - 1], nums[i]
            reverse(k, n - 1)
        print(nums)


s = Solution()
s.nextPermutation([1, 2, 3])
s.nextPermutation([0, 1, 2, 5, 3, 3, 0])
