class Solution:
    def reorderSpaces(self, text: str) -> str:
        n = text.count(' ')
        s = [c.strip() for c in text.split(" ") if c.strip() != '']
        if len(s) == 1:
            return text.strip() + ' ' * n
        x = n // (len(s) - 1)
        sep = ' ' * x
        return sep.join(s) + ' ' * (n % (len(s) - 1))


s = Solution()
print(s.reorderSpaces("  hello"))
