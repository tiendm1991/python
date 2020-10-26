class Solution:
    def trap(self, height) -> int:
        n = len(height)
        if n < 2:
            return 0
        result = 0
        stack = []
        for i in range(n):
            if not stack:
                stack.append(i)
            elif height[i] < height[stack[-1]]:
                stack.append(i)
            else:
                while stack and height[stack[-1]] <= height[i]:
                    x = height[stack.pop()]
                    if stack:
                        result += (min(height[stack[-1]], height[i]) - x) * (i - stack[-1] - 1)
                stack.append(i)
        return result


s = Solution()
print(s.trap([0, 1, 0, 3, 2, 1, 0, 1, 3, 2, 2, 2, 1]))
# print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
