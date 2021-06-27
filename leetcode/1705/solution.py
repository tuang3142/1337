from heapq import heappush as push
from heapq import heappop as pop

class Solution:
    def eatenApples(self, apples, days):
        i, n = 0, len(apples)
        eat = 0
        qu = []
        while i < n or qu:
            if i < n: push(qu, (i + days[i], apples[i]))
            while qu and (qu[0][0] <= i or qu[0][1] == 0):
                pop(qu)
            exp, app = pop(qu)
            i += 1
            app -= 1
            push(qu, (exp, app))
            eat += 1
        return eat
