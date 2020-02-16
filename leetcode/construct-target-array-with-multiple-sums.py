class Solution:
    def isPossibleBacktrack(self, target) -> bool:
        n = len(target)
        if n == 1:
            return target[0] == 1
        def backtrack(target, arr, s):
            check = True
            for i in range(len(arr)):
                if arr[i] > target[i]:
                    return False
                elif arr[i] < target[i]:
                    check = False
            if check:
                return True
            for i in range(len(arr)):
                tmp = arr[i]
                arr[i] = s
                if backtrack(target, arr, 2 * s - tmp):
                    return True
                arr[i] = tmp
            return False
        return backtrack(target, [1] * len(target), len(target))

    def isPossibleFaster(self, target) -> bool:
        n = len(target)
        if n == 1:
            return target[0] == 1
        def help(target):
            target.sort()
            s = sum(target[:n-1])
            if target[-1] == 1:
                return True
            elif target[-1] <= s:
                return False
            else:
                target[-1] -= s
                return help(target)
        return help(target)
s = Solution()
print(s.isPossibleFaster([1, 13, 19]))
