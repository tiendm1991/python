from datetime import datetime


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack, d = [], {}
        for num in nums2:
            if not stack or stack[-1] > num:
                stack.append(num)
                continue
            while len(stack) > 0 and stack[-1] < num:
                d[stack.pop()] = num
            stack.append(num)
        for num in stack:
            d[num] = -1
        return [d[num] for num in nums1]


s = Solution()
startTime = datetime.now()
print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
print(datetime.now() - startTime)
