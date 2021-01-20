import collections
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        n = len(S)
        d = collections.Counter(S)
        q = []
        for x in d:
            q.append([-d[x], x])
        heapq.heapify(q)
        ans = ""
        i = 0
        while i < n:
            x = ''
            push_back = []
            while q and x == '':
                candidate = heapq.heappop(q)
                if i > 0 and candidate[1] == ans[-1]:
                    push_back.append(candidate)
                else:
                    x = candidate[1]
                    candidate[0] += 1
                    if candidate[0] < 0:
                        push_back.append(candidate)
            if x == '':
                return ""
            ans += x
            i += 1
            for back in push_back:
                heapq.heappush(q, back)
        return ans


s = Solution()
print(s.reorganizeString("aaabc"))
