class Solution:
    def spellchecker(self, wordlist, queries):
        res = [""] * len(queries)
        words = {w for w in wordlist}
        caps = {}
        for w in wordlist:
            lower = w.lower()
            if lower not in caps:
                caps[lower] = w
        wrong_vowels = {}
        for w in wordlist:
            k = tuple('*' if c in 'aeiouAEIOU' else c.lower() for c in w)
            if k not in wrong_vowels:
                wrong_vowels[k] = w
        for i, q in enumerate(queries):
            if q in words:
                res[i] = q
            elif q.lower() in caps:
                res[i] = caps[q.lower()]
            else:
                k = tuple('*' if c in 'aeiouAEIOU' else c.lower() for c in q)
                res[i] = wrong_vowels.get(k, "")
        return res


s = Solution()
print(s.spellchecker(["KiTe", "kite", "hare", "Hare"],
                     ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]))
