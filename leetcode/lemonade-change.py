class Solution:
    def lemonadeChange(self, bills) -> bool:
        count = {5: 0, 10: 0}
        for x in bills:
            if x == 5:
                count[5] += 1
            else:
                if count[5] == 0:
                    return False
                if x == 10:
                    count[5] -= 1
                    count[10] += 1
                else:
                    if count[10] > 0:
                        count[10] -= 1
                        count[5] -= 1
                    elif count[5] < 3:
                        return False
                    else:
                        count[5] -= 3
        return True


s = Solution()
print(s.lemonadeChange([5, 5, 5, 10, 20]))
