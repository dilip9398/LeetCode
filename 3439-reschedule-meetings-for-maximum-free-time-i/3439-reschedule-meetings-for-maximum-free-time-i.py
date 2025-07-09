class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        time=0
        free=[]
        for i in range(len(startTime)):
            free.append(startTime[i]-time)
            time=endTime[i]
        free.append(eventTime-time)
        
        k+=1
        sums=sum(free[:k])
        ans=sums
        for i in range(k,len(free)):
            sums-=free[i-k]
            sums+=free[i]
            ans=max(ans,sums)
        return ans