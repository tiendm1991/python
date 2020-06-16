def getKmp(pattern):
    n = len(pattern)
    if n == 0:
        return ''
    result = [0] * n
    i, j = 1, 0
    while i < n:
        if pattern[i] == pattern[j]:
            result[i] = j + 1
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = result[j - 1]
    return result


def search(s, p):
    pattern = getKmp(p)
    i, j = 0, 0
    while i < len(s) - len(p):
        if s[i] == p[j]:
            if j == len(p) - 1:
                return True
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = pattern[j - 1]
    return False

print(search('cxzcabcedkvlsfamcl', 'abcd'))
