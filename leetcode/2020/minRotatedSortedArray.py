class Solution:
    def findMin(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return None

        def search(left, right):
            if right - left == 1:
                return min(nums[left], nums[right])
            if left == right:
                return nums[left]
            mid = (left + right) // 2

            if nums[left] == nums[mid]:
                if nums[mid] == nums[right]:
                    return search(left + 1, right - 1)
                elif nums[mid] < nums[right]:
                    return search(left + 1, mid)
                else:
                    return search(mid + 1, right)
            elif nums[left] < nums[mid]:
                if nums[mid] <= nums[right]:
                    return nums[left]
                else:
                    return search(mid + 1, right)
            else:
                return search(left + 1, mid)

        return search(0, n - 1)


s = Solution()
print(s.findMin([3, 3, 1, 3]))
