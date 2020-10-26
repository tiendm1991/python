import collections


class Solution:
    def displayTable(self, orders):
        n = len(orders)
        if n == 0:
            return []
        table = sorted(set([orders[i][1] for i in range(n)]), key=lambda x: int(x))
        food = sorted(set([orders[i][2] for i in range(n)]))
        result = []
        title = ['Table']
        for f in food:
            title.append(f)
        result.append(title)
        d = {}
        for order in orders:
            key = order[1] + '-' + order[2]
            if key not in d:
                d[key] = 1
            else:
                d[key] += 1
        for t in table:
            row = [t]
            for f in food:
                key = t + '-' + f
                if key not in d:
                    row.append("0")
                else:
                    row.append(str(d[key]))
            result.append(row)
        return result


s = Solution()
print(s.displayTable([["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
                      ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]))
