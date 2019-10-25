def countSubsequencesAiBjCk(s):
    n = len(s)
    count = 0
    nA, nB, nC = 0,0,0
    for i in range(n):
        if s[i] == 'a':
            nA += nA + 1
        elif s[i] == 'b':
            nB += nB + nA
        else:
            nC += nC + nB
    return nC

print(countSubsequencesAiBjCk('abbc'))
#abc, abc, abbc
print(countSubsequencesAiBjCk('bababc'))
# abc, abc, abbc, aabc, abc
print(countSubsequencesAiBjCk('abcabc'))
print(countSubsequencesAiBjCk('bababcac'))

