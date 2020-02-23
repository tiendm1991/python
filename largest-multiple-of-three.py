from string import digits


class Solution:
    def largestMultipleOfThree(self, digits) -> str:
        d = sorted([x for x in digits if x % 3 != 0], key=None, reverse=True)
        s = {1:0, 2:0, 4:0, 5:0, 7:0, 8:0}
        set2 = []
        set1 = []
        result = [x for x in digits if x % 3 == 0]
        a = 0
        tmp = result[::]
        for x in d:
            result.append(x)
            a += x
        mod = a % 3
        if mod != 0:
            idx = len(result) - 1
            while result[idx] % 3 != mod and idx >= 0:
                idx -= 1
            if idx >= 0:
                del result[idx]
            else:
                result = tmp
        if len(result) == 0:
            return ''
        result = sorted(result, key=None, reverse=True)
        if result[0] == 0:
            return '0'
        return ''.join([str(x) for x in result])

s = Solution()
print(s.largestMultipleOfThree([9,8,6,8,6]))