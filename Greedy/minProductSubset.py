def minProductSubset(a):
    n = len(a)
    c = min(a)
    if c >= 0:
        return c
    m_neg, m_pos, mg = 1, 1, a[0]

    for i in range(n):
        x = a[i]
        if x == 0:
            mg = min(m_neg, 0)
            m_neg, m_pos = 1, 1
        elif x < 0:
            tmp = m_neg
            m_neg = m_pos * x
            m_pos = max(tmp * x, 1)
            mg = min(mg, m_neg)
        else:
            m_neg = min(1, m_neg * x)
            m_pos *= x
            mg = min(mg, m_neg)
    return mg


print (minProductSubset([2, -2, -2, -1, -2, 4, 3]))
print (minProductSubset([-1, -1, -2, 4, 3]))
print (minProductSubset([-1, 0]))
print (minProductSubset([0, 0, 0]))

