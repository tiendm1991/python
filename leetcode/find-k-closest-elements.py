class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left, right = 0, n - k
        while left < right:
            mid = (left + right) // 2
            if mid + k >= n:
                right = mid - 1
                continue
            if x - arr[mid] > arr[mid+k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left: left + k]
