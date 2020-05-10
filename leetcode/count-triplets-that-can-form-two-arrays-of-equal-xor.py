class Solution:
    def countTriplets1(self, arr) -> int:
        n = len(arr)
        pre = [0] * (n+1)
        for i in range(1, n+1):
            pre[i] = pre[i-1] ^ arr[i-1]
        count = 0
        for i in range(1, n):
            for k in range(i+1, n+1):
                for j in range(i+1, k+1):
                    a = pre[j-1] ^ pre[i-1]
                    b = pre[j-1] ^ pre[k]
                    if a == b:
                        count += 1
        return count

    def countTriplets(self, arr) -> int:
        n = len(arr)
        count = 0
        for i in range(n-1):
            x = arr[i]
            for j in range(i+1, n):
                x ^= arr[j]
                if x == 0:
                    count += j - i
        return count
s = Solution()
print(s.countTriplets([1,1,1,1,1]))