class WordFilter:

    def __init__(self, words):
        self.d1 = {}  # map of array
        self.d2 = {}  # map of set
        for i, w in enumerate(words):
            n = len(w)
            for j in range(1, n + 1):
                s1 = w[:j]
                if s1 in self.d1:
                    self.d1[s1].append(i)
                else:
                    self.d1[s1] = [i]
                s2 = w[j - 1:]
                if s2 in self.d2:
                    self.d2[s2].add(i)
                else:
                    self.d2[s2] = {i}

    def f(self, prefix: str, suffix: str) -> int:
        if prefix not in self.d1 or suffix not in self.d2:
            return -1
        a = self.d1[prefix]
        for i in range(len(a) - 1, -1, -1):
            if a[i] in self.d2[suffix]:
                return a[i]
        return -1


obj = WordFilter(
    ["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa",
     "accabaccaa", "cabcbbbcca", "ababccabcb", "caccbbcbab", "bccbacbcba"])
print(obj.f("cac", "bab"))
