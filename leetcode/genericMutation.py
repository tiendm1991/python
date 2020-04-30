def valid(prev, next):
    x = 0
    for i in range(8):
        if prev[i] != next[i]:
            x += 1
    return x == 1


def minimumGeneticMutation(startStr, endStr, bank):
    q = [startStr]
    visited = set()
    count = 1
    while q:
        newQ = []
        for s in q:
            for g in bank:
                if valid(s, g) and g not in visited:
                    if g == endStr:
                        return count
                    newQ.append(g)
            visited.add(s)
        count += 1
        q = newQ
    return -1

startStr = 'AAAAAAAA'
endStr = 'CCCCCCCC'
bank =["AAAAAAAA",
 "AAAAAAAC",
 "AAAAAACC",
 "AAAAACCC",
 "AAAACCCC",
 "AACACCCC",
 "ACCACCCC",
 "ACCCCCCC",
 "CCCCCCCA"]
print(minimumGeneticMutation(startStr, endStr, bank))