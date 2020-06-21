class Solution:
    def getFolderNames(self, names):
        d = {}
        result = []
        for name in names:
            if name not in d:
                result.append(name)
                d[name] = 0
            else:
                while True:
                    d[name] += 1
                    x = name + '(' + str(d[name]) + ')'
                    if x not in d:
                        result.append(x)
                        d[x] = 0
                        break
        return result

s = Solution()
print(s.getFolderNames(["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]))
