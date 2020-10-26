class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        delta = 1 + 8 * target
        n = math.ceil((-1 + math.sqrt(delta)) / 2)
        A = n * (n + 1) // 2
        if A == target:
            return n
        while (A - target) % 2 == 1:
            n += 1
            A += n
        return n
