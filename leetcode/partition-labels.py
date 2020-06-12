class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chars = 'abcdefghijklmnopqrstuvwxyz'
        d = {c: 0 for c in chars}
        for i, c in enumerate(s):
            d[c] = i
        result = []
        start = 0
        _max = -1
        for i, c in enumerate(s):
            _max = max(_max, d[c])
            if _max == i:
                result.append(i - start + 1)
                start = i + 1
        return result
