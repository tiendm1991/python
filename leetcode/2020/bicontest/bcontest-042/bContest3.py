class Solution:
    def maximumBinaryString_long(self, binary: str) -> str:
        n = len(binary)
        if n == 1:
            return binary
        i = binary.find('0')
        if i == -1:
            return binary
        j = i + 1
        a = [c for c in binary]
        while j < n:
            if a[j] == '1':
                j += 1
            else:
                if j == i + 1:
                    a[i] = '1'
                    i = j
                    j += 1
                else:
                    a[i] = '1'
                    a[i + 1] = '0'
                    a[j] = '1'
                    i += 1
                    j += 1
        return ''.join(a)

    def maximumBinaryString(self, binary: str) -> str:
        n = len(binary)
        if n == 1:
            return binary
        i = binary.find('0')
        if i == -1:
            return binary
        j = i + 1
        a = [c for c in binary]
        while j < n:
            if a[j] == '1':
                j += 1
            else:
                a[i] = '1'
                a[i + 1] = '0'
                if j > i + 1:
                    a[j] = '1'
                i += 1
                j += 1
        return ''.join(a)


s = Solution()
print(s.maximumBinaryString_long("000110"), s.maximumBinaryString("000110"))
print(s.maximumBinaryString_long("01110"), s.maximumBinaryString("01110"))
