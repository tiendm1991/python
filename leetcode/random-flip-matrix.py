import random
class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.r = n_rows
        self.c = n_cols
        self.exist = set()
        
    def flip(self) -> List[int]:
        n = self.c * self.r
        if len(self.exist) == n:
            return None
        x = random.randrange(0, n)
        while x in self.exist:
            x = random.randrange(0, n)
        self.exist.add(x)
        return [x // self.c, x % self.c]

    def reset(self) -> None:
        self.exist = set()
        return None


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
