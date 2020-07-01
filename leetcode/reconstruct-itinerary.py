import functools
from datetime import datetime, time
import math


class Solution:
    def findItinerary1(self, tickets):
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
    
    
     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = {}
        for t in tickets:
            if t[0] not in d:
                d[t[0]] = [[t[1], False]]
            else:
                d[t[0]].append([t[1], False])
        for k in d:
            d[k].sort()


        def backtrack(d, result):
            if len(result) == len(tickets) + 1:
                return result
            cur = result[-1]
            if cur not in d:
                return None
            for x in d[cur]:
                if x[1]:
                    continue
                x[1] = True
                result.append(x[0])
                check = backtrack(d, result)
                if check:
                    return result
                else:
                    result.pop()
                    x[1] = False
            return None

        return backtrack(d, ['JFK'])
    
s = Solution()
startTime = datetime.now()
print(s.findItinerary([["EZE","TIA"],["EZE","AXA"],["AUA","EZE"],["EZE","JFK"],["JFK","ANU"],["JFK","ANU"],["AXA","TIA"],["JFK","AUA"],["TIA","JFK"],["ANU","EZE"],["ANU","EZE"],["TIA","AUA"]]))
print(s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(s.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
print(s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(datetime.now() - startTime)

