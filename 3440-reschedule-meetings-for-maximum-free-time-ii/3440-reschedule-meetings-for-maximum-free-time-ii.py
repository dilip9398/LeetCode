class Solution(object):
    def maxFreeTime(self,eventTime, startTime, endTime):
        n = len(startTime)
        meetings = (zip(startTime, endTime))
        durations = []
        gaps = []
        prev_end = 0 
        for i in range(n):
            # get gaps (to check if any space can move to)
            gaps.append(meetings[i][0]-prev_end)
            prev_end = meetings[i][1]
            # cal duration
            durations.append(meetings[i][1] - meetings[i][0])
        gaps.append(eventTime -meetings[-1][1] )
        # check all gaps
        counter = Counter(gaps)


        # get max space, add 0 to avoid that at least one max answer can be  choosed
        max_keys = sorted(list(counter.keys())+[0,0,0])[-3:]

        ans = 0 
        for ind, dur in enumerate(durations):
            # remove left and right space (neightbor)
            counter[gaps[ind]] -=1
            if counter[gaps[ind]] == 0:
                del counter[gaps[ind]]
            counter[gaps[ind+1]] -=1
            if counter[gaps[ind+1]] == 0:
                del counter[gaps[ind+1]]
            
            # get remanining max gaps
            max_gap = 0 
            for key in max_keys[::-1]:
                if counter.get(key, False):
                    max_gap = key
                    break

            if dur <= max_gap:
                ans = max(ans, gaps[ind]+dur+gaps[ind+1])
            else:
                ans = max(ans, gaps[ind]+gaps[ind+1])
            
            # Add key back
            counter[gaps[ind]] = counter[gaps[ind]] + 1  if counter.get(gaps[ind], False) else 1
            counter[gaps[ind+1]] = counter[gaps[ind+1]] + 1  if counter.get(gaps[ind+1], False) else 1
        return ans
            