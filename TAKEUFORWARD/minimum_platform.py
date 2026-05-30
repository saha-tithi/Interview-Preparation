class Solution:
    def findPlatform(self, Arrival, Departure):
        Arrival.sort()
        Departure.sort()
        i=0
        j=0
        platform=0
        max_platform=0

        while(i<(len(Arrival))):
            if Arrival[i]<=Departure[j]:
                platform=platform+1
                i=i+1
            else:
                platform=platform-1
                j=j+1
            max_platform=max(max_platform,platform)
        return max_platform