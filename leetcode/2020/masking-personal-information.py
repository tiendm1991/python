class Solution:
    def maskPII(self, S: str) -> str:
        def maskMail(s):
            a = s.split("@")
            a[0] = a[0][0] + "*" * 5 + a[0][-1]
            return '@'.join(a)

        def maskPhone(s):
            a = [c for c in s if c in '0123456789']
            if len(a) == 10:
                return "***-***-" + ''.join(a[-4:])
            else:
                return "+" + '*' * (len(a) - 10) + "-***-***-" + ''.join(a[-4:])

        if '@' in S:
            return maskMail(S.lower())
        else:
            return maskPhone(S)
