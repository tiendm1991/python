class Solution:
    def totalFruit(self, tree) -> int:
        n = len(tree)
        if n <= 2:
            return n
        res = 0
        stack = [tree[0]]
        s = {tree[0]}
        for i in range(1, n):
            x = tree[i]
            s.add(x)
            if len(s) <= 2:
                stack.append(x)
            else:
                res = max(res, len(stack))
                newStack = []
                tmp = stack[-1]
                while stack and stack[-1] == tmp:
                    newStack.append(stack.pop())
                stack = newStack
                newStack.append(x)
                s = {tmp, x}
        return max(res, len(stack))


s = Solution()
print(s.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
print(s.totalFruit([1, 2, 3, 2, 2]))
print(s.totalFruit([1, 1, 1]))
