from datetime import datetime, time
import heapq
import math

class Solution:
    def largestRectangleArea(self, h) -> int:
        if h == []:
            return 0
        _max = 0
        stack = []
        for i in range(len(h)):
            x = h[i]
            if not stack or h[stack[-1]] <= x:
                stack.append(i)
                continue
            n = len(stack)
            for k in range(n):
                _max = max(_max, h[stack[k]] * (stack[-1] - stack[k] + 1))
            j = n
            while j > 0 and h[stack[j-1]] >= x:
                j -= 1
            del stack[j+1:]
            h[stack[-1]] = x
            stack.append(i)
        for k in range(len(stack)):
            _max = max(_max, h[stack[k]] * (stack[-1] - stack[k] + 1))
        return _max

    def largestRectangleArea2(self, heights) -> int:
        if heights == []:
            return 0
        _max = 0
        stack = []
        for i in range(len(heights)):
            x = heights[i]
            while stack and heights[stack[-1]] >= x:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                _max = max(_max, h * w)
            stack.append(i)
        n = len(heights)
        while stack:
            h = heights[stack.pop()]
            w = n if not stack else n - stack[-1] - 1
            _max = max(_max, h * w)
        return _max
	
    def largestRectangleArea3(self, heights: List[int]) -> int:
        if heights == []:
            return 0
        _max = 0
        stack = []
        for i in range(len(heights)):
            x = heights[i]
            while stack and heights[stack[-1]] > x:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                _max = max(_max, h * w)
            stack.append(i)
        n = len(heights)
        pre = -1
        for i in range(len(stack)):
            h = heights[stack[i]]
            if h == 0:
                pre = stack[i]
                continue
            _max = max(_max, h * (n - (pre + 1)))
            pre = stack[i]

        return _max

s = Solution()
startTime = datetime.now()
print(s.largestRectangleArea([3,1,4,5,3,2,7,5,3]))
print(datetime.now() - startTime)

