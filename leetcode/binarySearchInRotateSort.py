from datetime import datetime


def search(nums, target) -> int:
    return binarySearch(nums, target, 0, len(nums) - 1)


def binarySearch(nums, target, left, right):
    if left > right:
        return -1
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    mid = (left + right + 1) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < nums[right]:
        if nums[mid] < target and nums[right] > target:
            return binarySearch(nums, target, mid + 1, right)
        else:
            return binarySearch(nums, target, left, mid - 1)
    else:
        if nums[left] < target and nums[mid] > target:
            return binarySearch(nums, target, left, mid - 1)
        else:
            return binarySearch(nums, target, mid + 1, right)


start = datetime.now()
print(search([4, 5, 6, 7, 0, 1, 2], 5))
print(datetime.now() - start)
# 01234567890123
# (()))())(

