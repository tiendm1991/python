import functools
from datetime import datetime, time
import math


class Solution:
    def numberToWords(self, num: int) -> str:
        mapping = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
                   10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
                   20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
        billion = 1000000000
        million = 1000000
        thousand = 1000
        hundred = 100
        x = ''
        def recursive(n):
            if n >= billion:
                x = recursive(n // billion).strip() + " Billion " + recursive(n % billion).strip()
                return x
            elif n >= million:
                x = recursive(n // million).strip() + " Million " + recursive(n % million).strip()
                return x
            elif n >= thousand:
                x = recursive(n // thousand).strip() +" Thousand " + recursive(n % thousand).strip()
                return x
            elif n >= hundred:
                x =  recursive(n // hundred).strip() + " Hundred " + recursive(n % hundred).strip()
                return x
            elif n >= 20:
                return mapping[(n // 10) * 10] + " " + mapping[n % 10]
            else:
                return mapping[n]
        if num == 0:
            return 'Zero'
        x = recursive(num)
        return x.strip()
s = Solution()
startTime = datetime.now()
print(s.numberToWords(100000))
print(datetime.now() - startTime)

