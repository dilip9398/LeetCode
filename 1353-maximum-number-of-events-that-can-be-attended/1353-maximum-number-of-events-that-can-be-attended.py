class Solution(object):
    def maxEvents(self, events):
        INF = 10 ** 20
        evt = collections.defaultdict(list)

        for s, e in events:
            evt[s].append(e)

        cnt = 0
        lt = -INF
        h =[]
        for t in sorted(evt.keys()):
            while len(h) > 0 and lt < t:
                e = heapq.heappop(h)
                if e >= lt:
                    cnt += 1
                    lt +=1
            lt = t

            for e in evt[t]:
                heapq.heappush(h, e)

            while len(h) > 0 and lt <= t:
                e = heapq.heappop(h)
                if e >= lt:
                    cnt += 1
                    lt +=1
                


        while len(h) > 0:
            e = heapq.heappop(h)
            if e >= lt:
                cnt += 1
                lt +=1
        
        return cnt


