class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k == n:
            return '0'
        stack = [num[0]]
        for i in range(1, n):
            while stack[-1] > num[i] and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[i])
        while k > 0:
            stack.pop()
            k -= 1
        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1
        if i == len(stack):
            return '0'
        return ''.join(stack[i:])


s = Solution()
startTime = datetime.now()
print(s.removeKdigits('1234567890', 4))
print(datetime.now() - startTime)
