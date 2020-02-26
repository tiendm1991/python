import functools
from datetime import datetime, time
import math


class Solution:
    def findItinerary(self, tickets):
        tickets = sorted(tickets, key = lambda x: x[1] + x[0])
        n = len(tickets)
        visited = [False] * n
        cur = 'JFK'
        result = [cur]
        def backtrack(n, result, visited, tickets,  cur):
            if len(result) == n+1:
                return result
            for i in range(n):
                if not visited[i] and tickets[i][0] == cur:
                    result.append(tickets[i][1])
                    cur = tickets[i][1]
                    visited[i] = True
                    check = backtrack(n, result, visited, tickets, cur)
                    if check != None:
                        return check
                    result.pop()
                    cur = result[-1]
                    visited[i] = False
            return None
        return backtrack(n, result, visited, tickets, cur)
s = Solution()
startTime = datetime.now()
print(s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
print(datetime.now() - startTime)

