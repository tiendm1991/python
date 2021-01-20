class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        def recursive(s):
            ans = []
            stack = [0]
            for x in s:
                if x == '1':
                    stack.append(stack[-1] + 1)
                else:
                    stack.append(stack[-1] - 1)
            start = 0
            i = 1
            # x, y = index of s, stack => x = y - 1
            while i < len(stack):
                if stack[i] == 0:
                    # substr(start + 1: i + 1)
                    # convert to index of s = substr(start, i)
                    if i - start == 2:
                        ans.append("10")
                    else:
                        ans.append('1' + recursive(s[start + 1: i - 1]) + '0')
                    start = i
                i += 1
            return ''.join(sorted(ans, reverse=True))

        return recursive(S)


s = Solution()
print(s.makeLargestSpecial("10101100"))
# 0 1 0 1 0 1 2 1 0
print(s.makeLargestSpecial("11011000"))
# 0 1 2 1 2 3 2 1 0
print(s.makeLargestSpecial("1011011000"))
# 0 1 0 1 2 1 2 3 2 1 0
